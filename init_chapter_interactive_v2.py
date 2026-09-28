#!/usr/bin/env python3
"""Интерактивная инициализация главы с единым корневым Julia-окружением.

Версия 3:
- StartMe.jl располагается в корне главы;
- имена каталогов и файлов создаются только латиницей, цифрами,
  символом подчеркивания и точкой в расширениях;
- краткое русское название хранится только в содержимом Markdown/YAML.
"""

from __future__ import annotations

import argparse
import re
from datetime import date
from pathlib import Path


def ascii_slug(value: str) -> str:
    """Преобразовать название в безопасный ASCII-идентификатор."""
    translit = {
        "а": "a", "б": "b", "в": "v", "г": "g", "д": "d", "е": "e",
        "ё": "e", "ж": "zh", "з": "z", "и": "i", "й": "j", "к": "k",
        "л": "l", "м": "m", "н": "n", "о": "o", "п": "p", "р": "r",
        "с": "s", "т": "t", "у": "u", "ф": "f", "х": "kh", "ц": "c",
        "ч": "ch", "ш": "sh", "щ": "shch", "ъ": "", "ы": "y", "ь": "",
        "э": "e", "ю": "yu", "я": "ya",
    }
    value = value.strip().lower()
    value = "".join(translit.get(char, char) for char in value)
    value = re.sub(r"[^a-z0-9]+", "_", value)
    return value.strip("_") or "chapter"


def ask_nonempty(prompt: str) -> str:
    while True:
        value = input(prompt).strip()
        if value:
            return value
        print("Поле не может быть пустым.")


def ask_number() -> str:
    while True:
        value = input("Введите номер главы: ").strip()
        if re.fullmatch(r"\d{1,3}", value):
            return value.zfill(2)
        print("Введите целое число от 1 до 999, например 2 или 02.")


def yaml_escape(value: str) -> str:
    return value.replace("\\", "\\\\").replace('"', '\\"').replace("\n", " ")


def chapter_markdown(number: str, title: str, chapter_id: str, comment: str) -> str:
    today = date.today().isoformat()
    return f'''---
title: "{yaml_escape(title)}"
short_title: "{yaml_escape(title)}"
chapter_id: "{chapter_id}"
chapter_number: "{number}"
version: "0.1.0"
status: "draft"
created: "{today}"
updated: "{today}"
comment: "{yaml_escape(comment)}"
julia_environment: "../../Project.toml"
reproducibility_status: "not_checked"
---

# {title}

> **Рабочий комментарий:** {comment}

## Навигация по материалам главы

| Раздел | Назначение |
|---|---|
| [Академическая справка](text/academic_note.md) | Научно-методическая характеристика темы, ее место в пособии и статус утверждений. |
| [Математическая модель](text/mathematical_model.md) | Рабочая постановка: переменные, параметры, единицы, уравнения и начальные условия. |
| [Вычислительный эксперимент](text/computational_experiment.md) | План эксперимента, сценарии, параметры запуска и критерии сравнения. |
| [Интерпретация](text/interpretation.md) | Биологический и математический анализ результатов. |
| [Ограничения](text/limitations.md) | Биологические, математические, численные, информационные и клинические ограничения. |
| [Julia](julia/) | Скрипты модели, экспериментов, визуализации и тесты. |
| [Pluto](pluto/) | Интерактивные учебные и экспериментальные блокноты. |
| [Данные](data/) | Исходные, обработанные данные и метаданные. |
| [Результаты](results/) | Таблицы, журналы запусков и производные вычислительные материалы. |
| [Графика](figures/) | Отрисованные графики в форматах SVG и PNG. |
| [Ресурсы](resources/) | Статьи, книги, веб-ресурсы, видео и разрешенные файлы для чтения. |
| [Методические материалы](teaching/) | Задания, контрольные вопросы, комментарии преподавателю, терминология и глоссарий. |
| [Источники](references/) | Библиография, интернет-ресурсы и реестр источников. |

## Аннотация

Кратко сформулируйте содержание, предметную область и основной результат главы.

## Учебные результаты

После изучения главы обучающийся сможет:

- сформулировать биомедицинскую задачу;
- описать допущения и переменные модели;
- реализовать модель на Julia;
- провести вычислительный эксперимент;
- интерпретировать результаты и ограничения.

## Биомедицинская задача

### Контекст

### Исследовательский вопрос

### Что моделируется и что не моделируется

## Допущения

| № | Допущение | Обоснование | Ограничение |
|---|---|---|---|
| 1 | | | |

## Переменные, параметры и единицы измерения

| Обозначение | Смысл | Тип | Единицы | Значение или диапазон | Источник |
|---|---|---|---|---|---|
| | | | | | |

## Математическая модель

### Переменные состояния

### Система уравнений

### Начальные условия

### Параметры и ограничения

### Аналитические свойства модели

## Реализация на Julia

Глава использует единое корневое окружение проекта. Запускайте скрипты из корня репозитория:

```bash
julia --project=. chapters/{chapter_id}/StartMe.jl
```

- [Корневой Project.toml](../../Project.toml)
- [Корневой Manifest.toml](../../Manifest.toml)
- [StartMe.jl](StartMe.jl)
- [Каталог Julia](julia/)
- [Основной скрипт](julia/main.jl)
- [Сценарии экспериментов](julia/run_experiments.jl)
- [Генерация графиков](julia/make_figures.jl)
- [Тесты](julia/tests/)

`StartMe.jl` расположен в корне главы, потому что он является конфигурационным входом всей главы, а не только одним из файлов исходного кода.

## Блокнот Pluto

- [Основной блокнот](pluto/01_main_model.jl)
- [Блокнот эксперимента](pluto/02_experiment.jl)
- [Инструкция по Pluto](pluto/README.md)

## Вычислительный эксперимент

### Цель эксперимента

### Сценарии

### План эксперимента

### Параметры запуска

### Критерии сравнения

## Результаты

- [Входные и обработанные данные](data/)
- [Таблицы результатов](results/tables/)
- [Журналы вычислений](results/logs/)
- [Графики SVG](figures/svg/)
- [Графики PNG](figures/png/)

## Интерпретация результатов

## Ограничения применимости

### Биологические ограничения

### Математические ограничения

### Численные ограничения

### Ограничения данных

### Ограничения клинической интерпретации

## Источники и дополнительные материалы

- [Основная литература](references/references_main.md)
- [Факультативная литература](references/references_optional.md)
- [Интернет-ресурсы и видео](references/online_resources.md)
- [Библиографическая база](references/bibliography.bib)
- [Реестр источников](references/source_registry.csv)
- [Материалы для чтения](resources/reading/)

## Контрольные вопросы и задания

- [Контрольные вопросы](teaching/questions.md)
- [Задания](teaching/assignments.md)

## Методические материалы

- [Комментарии для преподавателя](teaching/instructor_notes.md)
- [Термины и обозначения](teaching/terminology_table.md)
- [Перечень используемых моделей](teaching/model_inventory.md)
- [Глоссарий](teaching/glossary.md)

## Статус проверки

| Компонент | Статус | Ответственный | Дата | Комментарий |
|---|---|---|---|---|
| Текст | not_checked | | | |
| Код Julia | not_checked | | | |
| Pluto | not_checked | | | |
| Данные | not_checked | | | |
| Результаты | not_checked | | | |
| Графика | not_checked | | | |
| Источники | not_checked | | | |
| Методика | not_checked | | | |
'''


def startme_julia(number: str, title: str, chapter_id: str, comment: str) -> str:
    today = date.today().isoformat()
    return f'''"""
StartMe.jl — конфигурация главы {number}: {title}

Chapter ID: {chapter_id}
Created: {today}
Comment: {comment}

Запуск из корня репозитория:
    julia --project=. chapters/{chapter_id}/StartMe.jl

StartMe.jl расположен в корне главы и является единым входом для настройки
путей, каталогов результатов и базовой конфигурации главы.
"""

using Dates

const CHAPTER_NUMBER = "{number}"
const CHAPTER_TITLE = "{title.replace('"', '\\"')}"
const CHAPTER_ID = "{chapter_id}"

"""Найти корень проекта по наличию корневых Project.toml и Manifest.toml."""
function find_project_root(start::AbstractString = @__DIR__)
    current = abspath(start)
    while true
        if isfile(joinpath(current, "Project.toml")) &&
           isfile(joinpath(current, "Manifest.toml"))
            return current
        end
        parent = dirname(current)
        parent == current && error(
            "Не найден корень проекта с Project.toml и Manifest.toml. " *
            "Запустите скрипт из корректного репозитория."
        )
        current = parent
    end
end

const PROJECT_ROOT = find_project_root()
const CHAPTER_ROOT = joinpath(PROJECT_ROOT, "chapters", CHAPTER_ID)

isdir(CHAPTER_ROOT) || error("Каталог главы не найден: $CHAPTER_ROOT")

# Каталоги главы
const DIR_TEXT = joinpath(CHAPTER_ROOT, "text")
const DIR_JULIA = joinpath(CHAPTER_ROOT, "julia")
const DIR_PLUTO = joinpath(CHAPTER_ROOT, "pluto")
const DIR_DATA = joinpath(CHAPTER_ROOT, "data")
const DIR_DATA_RAW = joinpath(DIR_DATA, "raw")
const DIR_DATA_PROCESSED = joinpath(DIR_DATA, "processed")
const DIR_DATA_METADATA = joinpath(DIR_DATA, "metadata")
const DIR_RESULTS = joinpath(CHAPTER_ROOT, "results")
const DIR_RESULTS_TABLES = joinpath(DIR_RESULTS, "tables")
const DIR_RESULTS_LOGS = joinpath(DIR_RESULTS, "logs")
const DIR_FIGURES = joinpath(CHAPTER_ROOT, "figures")
const DIR_FIGURES_SVG = joinpath(DIR_FIGURES, "svg")
const DIR_FIGURES_PNG = joinpath(DIR_FIGURES, "png")
const DIR_RESOURCES = joinpath(CHAPTER_ROOT, "resources")
const DIR_REFERENCES = joinpath(CHAPTER_ROOT, "references")
const DIR_TEACHING = joinpath(CHAPTER_ROOT, "teaching")

const REQUIRED_DIRS = [
    DIR_TEXT, DIR_JULIA, DIR_PLUTO, DIR_DATA, DIR_DATA_RAW,
    DIR_DATA_PROCESSED, DIR_DATA_METADATA, DIR_RESULTS,
    DIR_RESULTS_TABLES, DIR_RESULTS_LOGS, DIR_FIGURES,
    DIR_FIGURES_SVG, DIR_FIGURES_PNG, DIR_RESOURCES,
    DIR_REFERENCES, DIR_TEACHING,
]

function ensure_directories!()
    foreach(mkpath, REQUIRED_DIRS)
    return nothing
end

function write_run_log!(; message::AbstractString = "StartMe.jl initialized")
    ensure_directories!()
    log_file = joinpath(DIR_RESULTS_LOGS, "startme.log")
    open(log_file, "a") do io
        println(io, "$(now()) | chapter=$(CHAPTER_ID) | $message")
    end
    return log_file
end

function show_config()
    println("Chapter $(CHAPTER_NUMBER): $(CHAPTER_TITLE)")
    println("Project root: $(PROJECT_ROOT)")
    println("Chapter root: $(CHAPTER_ROOT)")
    println("Data:         $(DIR_DATA)")
    println("Results:      $(DIR_RESULTS)")
    println("Figures SVG:  $(DIR_FIGURES_SVG)")
    println("Figures PNG:  $(DIR_FIGURES_PNG)")
end

ensure_directories!()
write_run_log!()
show_config()
'''


def files_for_chapter(number: str, title: str, chapter_id: str, comment: str) -> dict[str, str]:
    return {
        "README.md": f"# Chapter {number}: {title}\n\n{comment}\n\nMain file: [chapter.md](chapter.md).\n",
        "metadata.yaml": (
            f"chapter_id: {chapter_id}\nchapter_number: {number}\n"
            f"title: \"{yaml_escape(title)}\"\nstatus: draft\n"
            f"created: {date.today().isoformat()}\n"
            f"julia_environment: ../../Project.toml\n"
            f"comment: \"{yaml_escape(comment)}\"\n"
        ),
        "StartMe.jl": startme_julia(number, title, chapter_id, comment),
        "chapter.md": chapter_markdown(number, title, chapter_id, comment),
        "text/academic_note.md": "# Academic note\n\n## Topic\n\n## Modeling object\n\n## Modeling subject\n\n## Scientific and educational problem\n\n## Place in the book\n\n## Mathematical apparatus\n\n## Biological interpretation\n\n## Evidence status\n\n## Interpretation limits\n",
        "text/mathematical_model.md": "# Mathematical model\n\nDescribe variables, parameters, units, initial conditions, equations and model properties.\n",
        "text/computational_experiment.md": "# Computational experiment\n\nDescribe the question, scenarios, parameters, number of runs, comparison criteria and expected results.\n",
        "text/interpretation.md": "# Interpretation\n\nDescribe the biological meaning of trajectories, tables and figures.\n",
        "text/limitations.md": "# Limitations\n\nDescribe biological, mathematical, numerical, data and clinical limitations.\n",
        "julia/main.jl": "# Main chapter script\ninclude(joinpath(@__DIR__, \"..\", \"StartMe.jl\"))\n",
        "julia/run_experiments.jl": "# Experiment scenarios\ninclude(joinpath(@__DIR__, \"..\", \"StartMe.jl\"))\n",
        "julia/make_figures.jl": "# SVG and PNG generation\ninclude(joinpath(@__DIR__, \"..\", \"StartMe.jl\"))\n",
        "julia/tests/runtests.jl": "using Test\n\n@testset \"Chapter initialization\" begin\n    include(joinpath(@__DIR__, \"..\", \"..\", \"StartMe.jl\"))\n    @test isdir(DIR_RESULTS)\n    @test isdir(DIR_FIGURES_SVG)\n    @test isdir(DIR_FIGURES_PNG)\nend\n",
        "pluto/01_main_model.jl": "### A Pluto.jl notebook ###\n# v0.20.0\n\n\"\"\"\nMain educational notebook.\n\"\"\"\n\n",
        "pluto/02_experiment.jl": "### A Pluto.jl notebook ###\n# v0.20.0\n\n\"\"\"\nComputational experiment notebook.\n\"\"\"\n\n",
        "pluto/README.md": "# Pluto notebooks\n\nUse the root Julia environment of the repository.\n",
        "data/raw/README.md": "# Raw data\n\nRecord source, license, acquisition date, format and units.\n",
        "data/processed/README.md": "# Processed data\n\nDescribe transformations applied to raw data.\n",
        "data/metadata/README.md": "# Data metadata\n",
        "data/README.md": "# Data\n",
        "results/tables/README.md": "# Result tables\n",
        "results/logs/README.md": "# Run logs\n",
        "results/README.md": "# Results\n",
        "figures/svg/README.md": "# SVG figures\n",
        "figures/png/README.md": "# PNG figures\n",
        "figures/README.md": "# Figures\n",
        "resources/papers/README.md": "# Papers\n",
        "resources/books/README.md": "# Books and textbooks\n",
        "resources/web/README.md": "# Web resources\n",
        "resources/videos/README.md": "# Videos\n",
        "resources/reading/README.md": "# Reading files\n\nUse only materials with permitted redistribution or external links.\n",
        "resources/README.md": "# Resources\n",
        "teaching/assignments.md": "# Assignments\n\n## Basic\n\n## Intermediate\n\n## Advanced\n",
        "teaching/questions.md": "# Control questions\n\n1. What is the biomedical problem?\n2. What do the parameters mean?\n3. What are the model limitations?\n",
        "teaching/instructor_notes.md": "# Instructor notes\n\n## Learning goals\n\n## Sequence\n\n## Common errors\n\n## Assessment\n",
        "teaching/terminology_table.md": "# Terminology and notation\n\n| Term | Definition | Units | English equivalent | Usage |\n|---|---|---|---|---|\n| | | | | |\n",
        "teaching/model_inventory.md": "# Model inventory\n\n| Model | Type | Variables | Parameters | Question | Limitations | Files |\n|---|---|---|---|---|---|---|\n| | | | | | | |\n",
        "teaching/glossary.md": "# Glossary\n\n## Biological and medical terms\n\n## Mathematical terms\n\n## Programming and computational terms\n",
        "references/bibliography.bib": "% Chapter bibliography\n",
        "references/references_main.md": "# Main references\n",
        "references/references_optional.md": "# Optional references\n",
        "references/online_resources.md": "# Online resources and videos\n\n| Resource | Type | Author or organization | URL | Access date | Purpose |\n|---|---|---|---|---|---|\n| | | | | | |\n",
        "references/source_registry.csv": "source_id,claim_or_use,source_type,citation,doi_or_url,access_date,status,notes\n",
    }


def main() -> None:
    parser = argparse.ArgumentParser(description="Interactive creation of a chapter structure.")
    parser.add_argument("--root", default="chapters", help="Chapter root directory")
    parser.add_argument("--force", action="store_true", help="Overwrite existing files")
    args = parser.parse_args()

    print("Инициализация новой главы пособия")
    print("Для отмены нажмите Ctrl+C.\n")

    number = ask_number()
    title = ask_nonempty("Введите краткое название главы: ")
    comment = ask_nonempty("Введите комментарий: ")
    chapter_id = f"{number}_{ascii_slug(title)}"
    chapter_dir = Path(args.root) / chapter_id

    print("\nБудет создана структура:")
    print(f"  Номер:       {number}")
    print(f"  Название:    {title}")
    print(f"  Комментарий: {comment}")
    print(f"  Каталог:     {chapter_dir}")
    print("  Julia:       общее корневое окружение проекта")
    print("  Имена файлов: ASCII, без пробелов и специальных символов")

    if input("Создать структуру? [д/н]: ").strip().lower() not in {"д", "да", "y", "yes"}:
        print("Создание отменено.")
        return

    if chapter_dir.exists() and not args.force:
        raise SystemExit(
            f"Каталог уже существует: {chapter_dir}. "
            "Используйте --force только для осознанной перезаписи."
        )

    for relative_path, content in files_for_chapter(number, title, chapter_id, comment).items():
        path = chapter_dir / relative_path
        path.parent.mkdir(parents=True, exist_ok=True)
        if not path.exists() or args.force:
            path.write_text(content, encoding="utf-8")

    print(f"\nСтруктура создана: {chapter_dir}")
    print(f"Запуск:     julia --project=. {chapter_dir / 'StartMe.jl'}")
    print(f"Основной текст: {chapter_dir / 'chapter.md'}")


if __name__ == "__main__":
    main()
