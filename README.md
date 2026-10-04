# biomedical-modeling-julia

Учебное пособие по **компьютерному моделированию в биологии и медицине** на языке
программирования **Julia**. Ориентировано на студентов и преподавателей
медико-биологических направлений: от постановки математической модели до
вычислительного эксперимента, интерпретации результатов и оформления главы.

Автор: Самаркин Александр Иванович, Псковский государственный университет (ПсковГУ).

## Что уже готово

- **Единое Julia-окружение** на весь проект — [`Project.toml`](Project.toml) и
  [`Manifest.toml`](Manifest.toml) (DifferentialEquations, ModelingToolkit, Plots,
  CairoMakie, Pluto, DataFrames, CSV и др.). Все главы активируют именно его.
- **Глава 01 «Компьютерное моделирование и Julia»** —
  [`chapters/01_kompyuternoe_modelirovanie_i_julia/`](chapters/01_kompyuternoe_modelirovanie_i_julia/):
  основной текст в `chapter.qmd`, исходники Julia, Pluto-ноутбуки, методические
  материалы, реестр источников и структура данных/результатов/рисунков.
- **Генератор глав** — [`init_chapter_interactive_v2.py`](init_chapter_interactive_v2.py):
  создаёт новую главу с полным деревом каталогов, `StartMe.jl` и шаблонами.
- **Карта проекта** — [`FILES.md`](FILES.md): полный список ключевых файлов и
  папок с комментариями, обновляется скриптом [`tools/update_file_map.py`](tools/update_file_map.py).

## Быстрый старт

```bash
# 1. Установить окружение Julia (однократно)
julia --project=. -e 'using Pkg; Pkg.instantiate()'
# или через подготовленный скрипт
julia SetupProject.jl

# 2. Проверить конфигурацию главы и создать каталоги
julia --project=. chapters/01_kompyuternoe_modelirovanie_i_julia/StartMe.jl

# 3. Запустить тесты главы
julia --project=. chapters/01_kompyuternoe_modelirovanie_i_julia/julia/tests/runtests.jl
```

Сборка главы в HTML/PDF/DOCX выполняется через Quarto из каталога главы
(`_metadata.yaml` содержит настройки для всех трёх форматов).

## Обслуживание карты проекта

Полный порядок — в [`tools/README.md`](tools/README.md). Коротко: правьте описания
в [`tools/file_map_registry.md`](tools/file_map_registry.md) и пересчитывайте карту
одной командой (плановый интервал — раз в 3 дня):

```bash
python tools/update_file_map.py
```

<!-- FILE_MAP:START -->
<!-- Сгенерировано tools/update_file_map.py; не редактировать вручную. -->
### Ключевые файлы и папки

| Путь | Назначение |
|---|---|
| [Project.toml](Project.toml) | Единое Julia-окружение всего проекта: DifferentialEquations и OrdinaryDiffEq, ModelingToolkit, DataFrames и CSV, Distributions и StatsBase,… |
| [Manifest.toml](Manifest.toml) | Зафиксированные версии всех зависимостей (~152 КБ). Осознанно хранится в git — это основа воспроизводимости расчётов. |
| [SetupProject.jl](SetupProject.jl) | Первичная установка окружения: `Pkg.activate(".")` и `Pkg.add([...])` того же набора пакетов, что объявлен в Project.toml. |
| [init_chapter_interactive_v2.py](init_chapter_interactive_v2.py) | Интерактивный генератор новой главы (433 строки): спрашивает номер и название, транслитерирует их в ASCII-slug, создаёт дерево каталогов, S… |
| [pyproject.toml](pyproject.toml) | Python-обёртка (uv) вокруг этого генератора: пакет `biomedical-modeling-julia`, точка входа `biomedical-modeling-julia`, сборка через `uv_b… |
| [uv.lock](uv.lock) | Лок-файл uv. Внешних Python-зависимостей нет — только сам пакет проекта в editable-режиме. |
| [.python-version](.python-version) | Требуемая версия Python для uv (3.14). |
| [.gitignore](.gitignore) | Политика хранения: Project.toml и Manifest.toml отслеживаются; отслеживаются результаты `*.csv`, `*.svg`, `*.png`, `*.jld2`; игнорируются `… |
| [README.md](README.md) | Главная страница репозитория: назначение проекта, что уже готово, команды запуска и порядок обслуживания карты проекта (блок структуры обно… |
| [FILES.md](FILES.md) | Эта карта проекта: полный список ключевых файлов и папок с комментариями. Файл генерируется, править его вручную не нужно — правьте `tools/… |
| [AGENTS.md](AGENTS.md) | Постоянная память проекта для ИИ-ассистента: границы работы над текстом (содержание `chapter.qmd` — только по явному запросу, при неоднозна… |
| [УЧАСТНИКИ ПОРЯДОК РАБОТЫ.docx](<УЧАСТНИКИ ПОРЯДОК РАБОТЫ.docx>) | Организационный документ: состав участников проекта и регламент совместной работы. |
| [src](src/) | Исходники Python-пакета-обёртки. |
| [src/biomedical_modeling_julia](src/biomedical_modeling_julia/) | Пакет `biomedical_modeling_julia`, указанный как точка входа в pyproject.toml. |
| [src/biomedical_modeling_julia/__init__.py](src/biomedical_modeling_julia/__init__.py) | Заглушка пакета: функция `main()` печатает приветствие, нужна только для точки входа из pyproject.toml. |
| [tools](tools/) | Служебные скрипты сопровождения репозитория: реестр комментариев, генератор карты проекта и инструкция по их запуску. |
| [tools/README.md](tools/README.md) | Инструкция по обслуживанию карты: команды запуска, формат реестра, режим проверки и плановый интервал обновления. |
| [tools/update_file_map.py](tools/update_file_map.py) | Генератор карты проекта: читает реестр, обходит дерево репозитория, считает размеры и даты, пишет FILES.md и блок структуры в README.md. За… |
| [tools/file_map_registry.md](tools/file_map_registry.md) | Этот реестр: пути и текстовые пояснения, которые попадают в карту. |
| [chapters](chapters/) | Все главы пособия. Одна папка — одна глава; сейчас созданы главы 01 и 02. |

Полная карта со всеми разделами главы и статусами — в [FILES.md](FILES.md). Обновление: 2026-10-04, следующее по плану 2026-10-07 (раз в 3 дня).
<!-- FILE_MAP:END -->
