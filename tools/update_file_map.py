#!/usr/bin/env python3
"""Генератор карты проекта: FILES.md и блок структуры в README.md.

Описания берутся из реестра tools/file_map_registry.md, а структура, размеры
и даты пересчитываются по дереву репозитория при каждом запуске. Требует
только стандартную библиотеку Python (3.8+).

Использование (из корня репозитория):
    python tools/update_file_map.py             # обновить FILES.md и README.md
    python tools/update_file_map.py --check     # только проверить, не записывая
    python tools/update_file_map.py --quiet     # без вывода на экран

Плановый интервал обновления задаётся константой CADENCE_DAYS (по умолчанию 3 дня).
"""

from __future__ import annotations

import argparse
import fnmatch
import os
import re
import subprocess
import sys
from datetime import date, datetime, timedelta
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
REGISTRY = REPO_ROOT / "tools" / "file_map_registry.md"
OUTPUT = REPO_ROOT / "FILES.md"
README = REPO_ROOT / "README.md"

CADENCE_DAYS = 3
START_MARK = "<!-- FILE_MAP:START -->"
END_MARK = "<!-- FILE_MAP:END -->"

IGNORED_DIRS = {
    ".git", ".julia", ".juliaup", ".venv", "venv", "__pycache__",
    "node_modules", ".ipynb_checkpoints", ".pytest_cache",
    ".mypy_cache", ".ruff_cache", ".idea", ".vscode",
}
IGNORED_SUFFIXES = {".pyc", ".pyo", ".ji", ".swp", ".swo", ".tmp"}

# Файлы, которые генератор сам и создаёт: их размер не фиксируем в байтах,
# иначе размер карты меняется при каждом запуске и --check никогда не сходится.
SELF_GENERATED = {"README.md", "FILES.md"}


class Entry:
    __slots__ = ("path", "comment", "section", "opaque", "pattern", "is_dir")

    def __init__(self, path: str, comment: str, section: str, opaque: bool):
        self.path = path
        self.comment = comment
        self.section = section
        self.opaque = opaque
        self.pattern = any(ch in path for ch in "*?[")
        self.is_dir = path.endswith("/")


def parse_registry(text: str) -> list[Entry]:
    entries: list[Entry] = []
    section = ""
    in_fence = False
    for raw in text.splitlines():
        line = raw.rstrip()
        stripped = line.strip()
        if stripped.startswith("```"):
            in_fence = not in_fence
            continue
        if in_fence:
            continue
        if stripped.startswith("## "):
            section = stripped[3:].strip()
            continue
        if not stripped.startswith("- "):
            continue
        body = stripped[2:].strip()
        if " :: " not in body:
            continue
        path_part, comment = body.split(" :: ", 1)
        path_part = path_part.strip()
        comment = comment.strip()
        opaque = False
        if path_part.startswith("!"):
            opaque = True
            path_part = path_part[1:].strip()
        path = path_part.strip().lstrip("/")
        while path.startswith("./"):
            path = path[2:]
        path = path.replace("\\", "/")
        if path:
            entries.append(Entry(path, comment, section, opaque))
    return entries


def human_size(num: int) -> str:
    units = ["Б", "КБ", "МБ", "ГБ"]
    value = float(num)
    for unit in units:
        if value < 1024 or unit == units[-1]:
            if unit == "Б":
                return f"{int(value)} {unit}"
            return f"{value:.1f} {unit}".replace(".", ",")
        value /= 1024
    return f"{num} Б"


def plural(n: int, one: str, few: str, many: str) -> str:
    n = abs(n)
    if n % 100 in (11, 12, 13, 14):
        return many
    last = n % 10
    if last == 1:
        return one
    if 2 <= last <= 4:
        return few
    return many


def collect_tree() -> list[str]:
    """Относительные пути всех файлов и папок, без игнорируемых."""
    paths: list[str] = []
    for dirpath, dirnames, filenames in os.walk(REPO_ROOT):
        dirnames[:] = sorted(d for d in dirnames if d not in IGNORED_DIRS)
        for d in dirnames:
            paths.append((Path(dirpath) / d).relative_to(REPO_ROOT).as_posix())
        for f in sorted(filenames):
            if Path(f).suffix.lower() in IGNORED_SUFFIXES:
                continue
            paths.append((Path(dirpath) / f).relative_to(REPO_ROOT).as_posix())
    return paths


def file_date(rel: str) -> str:
    try:
        ts = (REPO_ROOT / rel).stat().st_mtime
        return datetime.fromtimestamp(ts).strftime("%Y-%m-%d")
    except OSError:
        return "—"


def dir_facts(rel: str):
    """(число файлов, суммарный размер, самая свежая дата) для папки."""
    base = REPO_ROOT / rel
    count = 0
    total = 0
    newest = 0.0
    if not base.is_dir():
        return None
    for dirpath, dirnames, filenames in os.walk(base):
        dirnames[:] = sorted(d for d in dirnames if d not in IGNORED_DIRS)
        for f in filenames:
            if Path(f).suffix.lower() in IGNORED_SUFFIXES:
                continue
            fp = Path(dirpath) / f
            try:
                st = fp.stat()
            except OSError:
                continue
            count += 1
            total += st.st_size
            newest = max(newest, st.st_mtime)
    date_str = (
        datetime.fromtimestamp(newest).strftime("%Y-%m-%d") if newest else "—"
    )
    return count, total, date_str


def facts_for(entry: Entry, tree: list[str]):
    """Возвращает (тип, подпись-факт, дата, существует)."""
    if entry.pattern:
        matches = [
            p for p in tree
            if fnmatch.fnmatch(p, entry.path) and (REPO_ROOT / p).is_file()
        ]
        if not matches:
            return ("маска", "нет совпадений", "—", False)
        size = sum((REPO_ROOT / p).stat().st_size for p in matches
                   if (REPO_ROOT / p).exists())
        newest = max(
            (REPO_ROOT / p).stat().st_mtime for p in matches
            if (REPO_ROOT / p).exists()
        )
        return (
            "маска",
            f"{len(matches)} {plural(len(matches), 'файл', 'файла', 'файлов')}, "
            f"{human_size(size)}",
            datetime.fromtimestamp(newest).strftime("%Y-%m-%d"),
            True,
        )
    if entry.is_dir:
        facts = dir_facts(entry.path)
        if facts is None:
            return ("папка", "не найдена", "—", False)
        count, total, date_str = facts
        return (
            "папка",
            f"{count} {plural(count, 'файл', 'файла', 'файлов')}, "
            f"{human_size(total)}",
            date_str,
            True,
        )
    target = REPO_ROOT / entry.path
    if target.is_file():
        # Собственные выходные файлы генератора не показываем в байтах:
        # их размер меняется при каждой перегенерации и не даёт карте сойтись.
        if entry.path in SELF_GENERATED:
            return ("файл", "генерируется", file_date(entry.path), True)
        return ("файл", human_size(target.stat().st_size), file_date(entry.path), True)
    if target.is_dir():
        facts = dir_facts(entry.path)
        if facts:
            count, total, date_str = facts
            return (
                "папка",
                f"{count} {plural(count, 'файл', 'файла', 'файлов')}, "
                f"{human_size(total)}",
                date_str,
                True,
            )
    return ("файл", "не найден", "—", False)


def is_covered(rel: str, entries: list[Entry]) -> bool:
    for e in entries:
        if e.pattern:
            if fnmatch.fnmatch(rel, e.path):
                return True
            continue
        base = e.path.rstrip("/")
        if rel == base:
            return True
        if e.opaque and e.is_dir and rel.startswith(base + "/"):
            return True
    return False


def link_for(path: str, is_dir: bool) -> str:
    label = path
    if is_dir:
        label = path.rstrip("/")
    if re.search(r"[\s()]", path) or any(ord(c) > 127 for c in path):
        return f"[{label}](<{path}>)"
    return f"[{label}]({path})"


def git_counts():
    try:
        out = subprocess.run(
            ["git", "ls-files"],
            cwd=str(REPO_ROOT),
            capture_output=True,
            text=True,
            check=True,
        ).stdout.splitlines()
        tracked = len([l for l in out if l.strip()])
    except Exception:
        tracked = None
    try:
        last = subprocess.run(
            ["git", "log", "-1", "--format=%cI"],
            cwd=str(REPO_ROOT),
            capture_output=True,
            text=True,
            check=True,
        ).stdout.strip()
    except Exception:
        last = None
    return tracked, last


def read_previous_update() -> str | None:
    if not OUTPUT.exists():
        return None
    text = OUTPUT.read_text(encoding="utf-8")
    m = re.search(r"\*\*Обновлено:\*\*\s*(\d{4}-\d{2}-\d{2})", text)
    return m.group(1) if m else None


def build_map(entries: list[Entry], tree: list[str], now: datetime,
              previous: str | None) -> str:
    tracked, last_commit = git_counts()
    total_files = sum(1 for p in tree if (REPO_ROOT / p).is_file())
    total_dirs = sum(1 for p in tree if (REPO_ROOT / p).is_dir())

    if previous:
        try:
            prev_date = datetime.strptime(previous, "%Y-%m-%d").date()
        except ValueError:
            prev_date = now.date()
    else:
        prev_date = now.date()
    next_due = prev_date + timedelta(days=CADENCE_DAYS)

    lines: list[str] = []
    lines.append("# Карта проекта: ключевые файлы и папки")
    lines.append("")
    lines.append("> **Сгенерировано автоматически:** `python tools/update_file_map.py`")
    lines.append(f"> **Обновлено:** {now.strftime('%Y-%m-%d')} · "
                 f"**Плановый интервал:** раз в {CADENCE_DAYS} дня · "
                 f"**Следующее обновление:** {next_due.isoformat()}")
    lines.append("> Описания берутся из реестра `tools/file_map_registry.md`; "
                 "структура, размеры и даты пересчитываются при каждом запуске. "
                 "Этот файл править вручную не нужно.")
    lines.append("")
    lines.append(f"В репозитории **{total_files} файлов** и **{total_dirs} папок**"
                 + (f", под контролем git — **{tracked} файлов**." if tracked is not None else "."))
    if last_commit:
        lines.append(f"Последний коммит: {last_commit[:10]}.")
    lines.append("")

    sections: dict[str, list[Entry]] = {}
    order: list[str] = []
    for e in entries:
        if e.section not in sections:
            sections[e.section] = []
            order.append(e.section)
        sections[e.section].append(e)

    for section in order:
        lines.append(f"## {section}")
        lines.append("")
        lines.append("| Путь | Тип / размер | Изменён | Комментарий |")
        lines.append("|---|---|---|---|")
        for e in sections[section]:
            kind, fact, changed, exists = facts_for(e, tree)
            if exists and not e.pattern:
                path_cell = link_for(e.path, e.is_dir or kind == "папка")
            else:
                path_cell = f"`{e.path}`" + ("" if exists else " ⚠")
            fact_cell = (f"{kind}, {fact}" if kind != "маска" else fact)
            lines.append(f"| {path_cell} | {fact_cell} | {changed} | {e.comment} |")
        lines.append("")

    uncovered = sorted(
        p for p in tree if not is_covered(p, entries)
    )
    stale = sorted(
        (e for e in entries
         if not e.pattern and not (REPO_ROOT / e.path.rstrip("/")).exists()),
        key=lambda e: e.path,
    )
    if uncovered:
        lines.append("## Не описано в реестре")
        lines.append("")
        lines.append("Эти пути существуют в дереве, но для них нет записи в "
                     "`tools/file_map_registry.md`. Добавьте строку и перезапустите генератор:")
        lines.append("")
        for p in uncovered:
            lines.append(f"- `{p}`")
        lines.append("")
    if stale:
        lines.append("## Устаревшие записи реестра")
        lines.append("")
        lines.append("Эти записи ссылаются на несуществующие пути — удалите или исправьте их:")
        lines.append("")
        for e in stale:
            lines.append(f"- `{e.path}` — {e.comment[:80]}")
        lines.append("")

    return "\n".join(lines).rstrip() + "\n"


def build_readme_block(entries: list[Entry], now: datetime, previous: str | None) -> str:
    root_section = next((s for e in entries if e.section.startswith("Корень") for s in [e.section]), "Корень репозитория")
    root_entries = [e for e in entries if e.section == root_section and not e.pattern]
    if previous:
        try:
            prev_date = datetime.strptime(previous, "%Y-%m-%d").date()
        except ValueError:
            prev_date = now.date()
    else:
        prev_date = now.date()
    next_due = prev_date + timedelta(days=CADENCE_DAYS)

    lines: list[str] = []
    lines.append("<!-- Сгенерировано tools/update_file_map.py; не редактировать вручную. -->")
    lines.append("### Ключевые файлы и папки")
    lines.append("")
    lines.append("| Путь | Назначение |")
    lines.append("|---|---|")
    for e in root_entries:
        comment = e.comment if len(e.comment) <= 140 else e.comment[:139] + "…"
        if e.is_dir:
            path_cell = link_for(e.path, True)
        else:
            path_cell = link_for(e.path, False)
        lines.append(f"| {path_cell} | {comment} |")
    lines.append("")
    lines.append(f"Полная карта со всеми разделами главы и статусами — в "
                 f"[FILES.md](FILES.md). Обновление: {now.strftime('%Y-%m-%d')}, "
                 f"следующее по плану {next_due.isoformat()} (раз в {CADENCE_DAYS} дня).")
    return "\n".join(lines)


def update_readme(block: str) -> None:
    if README.exists():
        text = README.read_text(encoding="utf-8")
    else:
        text = ""
    if START_MARK in text and END_MARK in text:
        pre = text.split(START_MARK, 1)[0]
        post = text.split(END_MARK, 1)[1]
        new_text = pre + START_MARK + "\n" + block + "\n" + END_MARK + post
    else:
        new_text = text.rstrip() + "\n\n" + START_MARK + "\n" + block + "\n" + END_MARK + "\n"
    README.write_text(new_text, encoding="utf-8", newline="\n")


def main() -> int:
    parser = argparse.ArgumentParser(description="Генератор карты проекта.")
    parser.add_argument("--check", action="store_true",
                        help="только проверить актуальность карты, ничего не писать")
    parser.add_argument("--quiet", action="store_true",
                        help="не печатать сводку")
    args = parser.parse_args()

    try:
        sys.stdout.reconfigure(encoding="utf-8")
    except Exception:
        pass

    if not REGISTRY.exists():
        print(f"Не найден реестр: {REGISTRY}", file=sys.stderr)
        return 2

    registry_text = REGISTRY.read_text(encoding="utf-8")
    entries = parse_registry(registry_text)
    if not entries:
        print("Реестр пуст — нечего генерировать.", file=sys.stderr)
        return 2

    now = datetime.now()
    previous = read_previous_update()
    tree = collect_tree()
    map_text = build_map(entries, tree, now, previous)
    readme_block = build_readme_block(entries, now, previous)

    if args.check:
        if OUTPUT.exists() and OUTPUT.read_text(encoding="utf-8") == map_text:
            if not args.quiet:
                print("Карта актуальна. Изменений нет.")
            return 0
        if not args.quiet:
            print("Карта устарела или отсутствует — запустите "
                  "`python tools/update_file_map.py` для обновления.")
        return 1

    OUTPUT.write_text(map_text, encoding="utf-8", newline="\n")
    update_readme(readme_block)

    if not args.quiet:
        print(f"Обновлено: FILES.md и блок структуры в README.md")
        print(f"Записей в реестре: {len(entries)}")
        total_files = sum(1 for p in tree if (REPO_ROOT / p).is_file())
        uncovered = sorted(p for p in tree if not is_covered(p, entries))
        print(f"Файлов в дереве: {total_files}; не описано: {len(uncovered)}")
        prev = read_previous_update()
        if prev:
            try:
                due = datetime.strptime(prev, "%Y-%m-%d").date() + timedelta(days=CADENCE_DAYS)
                if now.date() >= due:
                    print(f"⚠ Плановая дата обновления ({due.isoformat()}) наступила — "
                          f"обновление выполнено.")
                else:
                    print(f"Следующее плановое обновление: {due.isoformat()} "
                          f"(раз в {CADENCE_DAYS} дня).")
            except ValueError:
                pass
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
