# Карта проекта: ключевые файлы и папки

> **Сгенерировано автоматически:** `python tools/update_file_map.py`
> **Обновлено:** 2026-10-04 · **Плановый интервал:** раз в 3 дня · **Следующее обновление:** 2026-10-07
> Описания берутся из реестра `tools/file_map_registry.md`; структура, размеры и даты пересчитываются при каждом запуске. Этот файл править вручную не нужно.

В репозитории **177 файлов** и **65 папок**, под контролем git — **108 файлов**.
Последний коммит: 2026-10-04.

## Корень репозитория

| Путь | Тип / размер | Изменён | Комментарий |
|---|---|---|---|
| [Project.toml](Project.toml) | файл, 982 Б | 2026-10-01 | Единое Julia-окружение всего проекта: DifferentialEquations и OrdinaryDiffEq, ModelingToolkit, DataFrames и CSV, Distributions и StatsBase, Plots вместе с CairoMakie, Pluto, IJulia, JLD2, JSON, XLSX, Test. Главы активируют именно этот файл (`julia_environment: ../../Project.toml`). |
| [Manifest.toml](Manifest.toml) | файл, 151,7 КБ | 2026-10-01 | Зафиксированные версии всех зависимостей (~152 КБ). Осознанно хранится в git — это основа воспроизводимости расчётов. |
| [SetupProject.jl](SetupProject.jl) | файл, 361 Б | 2026-09-30 | Первичная установка окружения: `Pkg.activate(".")` и `Pkg.add([...])` того же набора пакетов, что объявлен в Project.toml. |
| [init_chapter_interactive_v2.py](init_chapter_interactive_v2.py) | файл, 20,6 КБ | 2026-09-30 | Интерактивный генератор новой главы (433 строки): спрашивает номер и название, транслитерирует их в ASCII-slug, создаёт дерево каталогов, StartMe.jl, chapter.md, _metadata.yaml и все шаблоны через `files_for_chapter()`. |
| [pyproject.toml](pyproject.toml) | файл, 433 Б | 2026-09-30 | Python-обёртка (uv) вокруг этого генератора: пакет `biomedical-modeling-julia`, точка входа `biomedical-modeling-julia`, сборка через `uv_build`. |
| [uv.lock](uv.lock) | файл, 154 Б | 2026-09-30 | Лок-файл uv. Внешних Python-зависимостей нет — только сам пакет проекта в editable-режиме. |
| [.python-version](.python-version) | файл, 6 Б | 2026-09-30 | Требуемая версия Python для uv (3.14). |
| [.gitignore](.gitignore) | файл, 2,1 КБ | 2026-09-30 | Политика хранения: Project.toml и Manifest.toml отслеживаются; отслеживаются результаты `*.csv`, `*.svg`, `*.png`, `*.jld2`; игнорируются `*.xlsx`, `*.parquet`, `*.h5`, `*.mat`, медиафайлы, содержимое `results/logs/` и все кэши. |
| [README.md](README.md) | файл, генерируется | 2026-10-04 | Главная страница репозитория: назначение проекта, что уже готово, команды запуска и порядок обслуживания карты проекта (блок структуры обновляется скриптом). |
| [FILES.md](FILES.md) | файл, генерируется | 2026-10-04 | Эта карта проекта: полный список ключевых файлов и папок с комментариями. Файл генерируется, править его вручную не нужно — правьте `tools/file_map_registry.md`. |
| [AGENTS.md](AGENTS.md) | файл, 9,1 КБ | 2026-10-04 | Постоянная память проекта для ИИ-ассистента: границы работы над текстом (содержание `chapter.qmd` — только по явному запросу, при неоднозначности спрашивать), роль (инженер, к.т.н., математическое моделирование в биомедицине), аудитория и стиль текстов, требования к коду и комментариям, технологический стек, правила работы с артефактами карты проекта. |
| [УЧАСТНИКИ ПОРЯДОК РАБОТЫ.docx](<УЧАСТНИКИ ПОРЯДОК РАБОТЫ.docx>) | файл, 405,7 КБ | 2026-09-30 | Организационный документ: состав участников проекта и регламент совместной работы. |
| [src](src/) | папка, 1 файл, 73 Б | 2026-09-30 | Исходники Python-пакета-обёртки. |
| [src/biomedical_modeling_julia](src/biomedical_modeling_julia/) | папка, 1 файл, 73 Б | 2026-09-30 | Пакет `biomedical_modeling_julia`, указанный как точка входа в pyproject.toml. |
| [src/biomedical_modeling_julia/__init__.py](src/biomedical_modeling_julia/__init__.py) | файл, 73 Б | 2026-09-30 | Заглушка пакета: функция `main()` печатает приветствие, нужна только для точки входа из pyproject.toml. |
| [tools](tools/) | папка, 3 файла, 47,9 КБ | 2026-10-04 | Служебные скрипты сопровождения репозитория: реестр комментариев, генератор карты проекта и инструкция по их запуску. |
| [tools/README.md](tools/README.md) | файл, 3,8 КБ | 2026-10-03 | Инструкция по обслуживанию карты: команды запуска, формат реестра, режим проверки и плановый интервал обновления. |
| [tools/update_file_map.py](tools/update_file_map.py) | файл, 18,0 КБ | 2026-10-03 | Генератор карты проекта: читает реестр, обходит дерево репозитория, считает размеры и даты, пишет FILES.md и блок структуры в README.md. Зависимостей нет, только стандартная библиотека Python. |
| [tools/file_map_registry.md](tools/file_map_registry.md) | файл, 26,0 КБ | 2026-10-04 | Этот реестр: пути и текстовые пояснения, которые попадают в карту. |
| [chapters](chapters/) | папка, 161 файл, 5,8 МБ | 2026-10-04 | Все главы пособия. Одна папка — одна глава; сейчас созданы главы 01 и 02. |

## Глава 01 — паспорт, сборка и артефакты

| Путь | Тип / размер | Изменён | Комментарий |
|---|---|---|---|
| [chapters/01_kompyuternoe_modelirovanie_i_julia](chapters/01_kompyuternoe_modelirovanie_i_julia/) | папка, 92 файла, 3,6 МБ | 2026-10-03 | Глава 01 «Компьютерное моделирование и Julia»: исходники текста, код, ноутбуки, данные, результаты и методические материалы. |
| [chapters/01_kompyuternoe_modelirovanie_i_julia/README.md](chapters/01_kompyuternoe_modelirovanie_i_julia/README.md) | файл, 245 Б | 2026-09-30 | Краткая карточка главы: название, тема и ссылка на основной файл chapter.md. |
| [chapters/01_kompyuternoe_modelirovanie_i_julia/_metadata.yaml](chapters/01_kompyuternoe_modelirovanie_i_julia/_metadata.yaml) | файл, 3,1 КБ | 2026-09-30 | Паспорт главы (номер, ID, статус draft, автор — ПсковГУ, дата) и настройки вывода Quarto для трёх форматов: HTML (тема easy, выключка по ширине), Typst/PDF (A4, Calibri, кастомные заголовки и колонтитул) и DOCX. |
| [chapters/01_kompyuternoe_modelirovanie_i_julia/chapter.qmd](chapters/01_kompyuternoe_modelirovanie_i_julia/chapter.qmd) | файл, 52,5 КБ | 2026-10-03 | Главный содержательный исходник главы (438 строк, движок jupyter): введение, зачем моделирование медикам, необходимый минимум математики, обзор средств моделирования. Править текст нужно прежде всего здесь. |
| [chapters/01_kompyuternoe_modelirovanie_i_julia/chapter.md](chapters/01_kompyuternoe_modelirovanie_i_julia/chapter.md) | файл, 8,1 КБ | 2026-09-30 | Markdown-версия главы с YAML-фронтматтером и навигацией по разделам. Метаданные дублируют `_metadata.yaml` — при правке следите, чтобы они не разошлись. |
| [chapters/01_kompyuternoe_modelirovanie_i_julia/chapter.html](chapters/01_kompyuternoe_modelirovanie_i_julia/chapter.html) | файл, 79,6 КБ | 2026-10-03 | Собранная HTML-версия главы. Генерируется Quarto, вручную не правится. |
| [chapters/01_kompyuternoe_modelirovanie_i_julia/chapter.pdf](chapters/01_kompyuternoe_modelirovanie_i_julia/chapter.pdf) | файл, 129,4 КБ | 2026-09-30 | Собранный PDF через Typst. Генерируется Quarto, вручную не правится. |
| [chapters/01_kompyuternoe_modelirovanie_i_julia/chapter.docx](chapters/01_kompyuternoe_modelirovanie_i_julia/chapter.docx) | файл, 37,9 КБ | 2026-09-30 | Собранный Word-документ. Генерируется Quarto, вручную не правится. |
| [chapters/01_kompyuternoe_modelirovanie_i_julia/custom-reference.docx](chapters/01_kompyuternoe_modelirovanie_i_julia/custom-reference.docx) | файл, 42,4 КБ | 2026-09-30 | Эталонный документ Word со стилями для DOCX-вывода (`reference-doc` в `_metadata.yaml`). |
| [chapters/01_kompyuternoe_modelirovanie_i_julia/chapter_files](chapters/01_kompyuternoe_modelirovanie_i_julia/chapter_files/) | папка, 15 файлов, 1,7 МБ | 2026-10-03 | Ресурсы HTML-рендера: Bootstrap, quarto-html, tippy, tabsets (~1,4 МБ). Полностью генерируется, править не нужно. |
| [chapters/01_kompyuternoe_modelirovanie_i_julia/.quarto](chapters/01_kompyuternoe_modelirovanie_i_julia/.quarto/) | папка, 1 файл, 6,4 КБ | 2026-09-30 | Системный кэш Quarto, в том числе список доступных шрифтов для Typst. |
| [chapters/01_kompyuternoe_modelirovanie_i_julia/sample1.md](chapters/01_kompyuternoe_modelirovanie_i_julia/sample1.md) | файл, 7,0 КБ | 2026-10-02 | Пример презентации в формате Marp — по теме диодов и электроники, то есть не по теме пособия. Кандидат на удаление или замену на биомедицинский пример. |
| [chapters/01_kompyuternoe_modelirovanie_i_julia/sample1.pdf](chapters/01_kompyuternoe_modelirovanie_i_julia/sample1.pdf) | файл, 134,1 КБ | 2026-10-02 | Собранный PDF той же презентации. |

## Глава 01 — код и вычисления

| Путь | Тип / размер | Изменён | Комментарий |
|---|---|---|---|
| [chapters/01_kompyuternoe_modelirovanie_i_julia/StartMe.jl](chapters/01_kompyuternoe_modelirovanie_i_julia/StartMe.jl) | файл, 3,7 КБ | 2026-09-30 | Центральный узел главы: ищет корень проекта по паре Project.toml + Manifest.toml, объявляет константы `DIR_*` (text, julia, pluto, data/raw, data/processed, data/metadata, results/tables, results/logs, figures/svg, figures/png, resources, references, teaching), создаёт каталоги, пишет журнал `results/logs/startme.log` и печатает конфигурацию. |
| [chapters/01_kompyuternoe_modelirovanie_i_julia/julia](chapters/01_kompyuternoe_modelirovanie_i_julia/julia/) | папка, 5 файлов, 1002 Б | 2026-10-03 | Скрипты главы. Запускаются из корня репозитория с ключом `--project=.`. |
| [chapters/01_kompyuternoe_modelirovanie_i_julia/julia/main.jl](chapters/01_kompyuternoe_modelirovanie_i_julia/julia/main.jl) | файл, 72 Б | 2026-09-30 | Заявленная точка входа главы. Пока заглушка: подключает StartMe.jl. |
| [chapters/01_kompyuternoe_modelirovanie_i_julia/julia/run_experiments.jl](chapters/01_kompyuternoe_modelirovanie_i_julia/julia/run_experiments.jl) | файл, 73 Б | 2026-09-30 | Сценарии вычислительного эксперимента. Пока заглушка вокруг StartMe.jl — здесь должна появиться логика прогонов и сохранения таблиц. |
| [chapters/01_kompyuternoe_modelirovanie_i_julia/julia/make_figures.jl](chapters/01_kompyuternoe_modelirovanie_i_julia/julia/make_figures.jl) | файл, 75 Б | 2026-09-30 | Генерация рисунков SVG и PNG для главы. Пока заглушка вокруг StartMe.jl. |
| [chapters/01_kompyuternoe_modelirovanie_i_julia/julia/sample1.jl](chapters/01_kompyuternoe_modelirovanie_i_julia/julia/sample1.jl) | файл, 565 Б | 2026-10-03 | Учебный пример построения фигуры Лиссажу на Plots (backend GR) — образец оформления кода для главы. |
| [chapters/01_kompyuternoe_modelirovanie_i_julia/julia/tests](chapters/01_kompyuternoe_modelirovanie_i_julia/julia/tests/) | папка, 1 файл, 217 Б | 2026-09-30 | Тесты главы. |
| [chapters/01_kompyuternoe_modelirovanie_i_julia/julia/tests/runtests.jl](chapters/01_kompyuternoe_modelirovanie_i_julia/julia/tests/runtests.jl) | файл, 217 Б | 2026-09-30 | Smoke-тест: после запуска StartMe.jl проверяет существование каталогов `DIR_RESULTS`, `DIR_FIGURES_SVG`, `DIR_FIGURES_PNG`. |
| [chapters/01_kompyuternoe_modelirovanie_i_julia/pluto](chapters/01_kompyuternoe_modelirovanie_i_julia/pluto/) | папка, 4 файла, 38,6 КБ | 2026-10-03 | Интерактивные ноутбуки Pluto главы. Работают в корневом Julia-окружении репозитория. |
| [chapters/01_kompyuternoe_modelirovanie_i_julia/pluto/README.md](chapters/01_kompyuternoe_modelirovanie_i_julia/pluto/README.md) | файл, 72 Б | 2026-09-30 | Напоминание, что ноутбуки используют корневое окружение. |
| [chapters/01_kompyuternoe_modelirovanie_i_julia/pluto/01_main_model.jl](chapters/01_kompyuternoe_modelirovanie_i_julia/pluto/01_main_model.jl) | файл, 82 Б | 2026-09-30 | Pluto-ноутбук с основной учебной моделью (каркас, формат v0.20.0). |
| [chapters/01_kompyuternoe_modelirovanie_i_julia/pluto/02_experiment.jl](chapters/01_kompyuternoe_modelirovanie_i_julia/pluto/02_experiment.jl) | файл, 90 Б | 2026-09-30 | Pluto-ноутбук вычислительного эксперимента (каркас). |

## Глава 01 — текст, методика и источники

| Путь | Тип / размер | Изменён | Комментарий |
|---|---|---|---|
| [chapters/01_kompyuternoe_modelirovanie_i_julia/text](chapters/01_kompyuternoe_modelirovanie_i_julia/text/) | папка, 5 файлов, 686 Б | 2026-09-30 | Смысловые блоки главы. Сейчас это шаблоны с одними заголовками — содержательная часть пока живёт в `chapter.qmd`. |
| [chapters/01_kompyuternoe_modelirovanie_i_julia/text/academic_note.md](chapters/01_kompyuternoe_modelirovanie_i_julia/text/academic_note.md) | файл, 250 Б | 2026-09-30 | Академическая справка: тема, объект и предмет моделирования, научно-методическая проблема, место главы в книге. |
| [chapters/01_kompyuternoe_modelirovanie_i_julia/text/mathematical_model.md](chapters/01_kompyuternoe_modelirovanie_i_julia/text/mathematical_model.md) | файл, 116 Б | 2026-09-30 | Рабочая постановка модели: переменные, параметры, единицы измерения, начальные условия, уравнения и свойства модели. |
| [chapters/01_kompyuternoe_modelirovanie_i_julia/text/computational_experiment.md](chapters/01_kompyuternoe_modelirovanie_i_julia/text/computational_experiment.md) | файл, 135 Б | 2026-09-30 | Описание вычислительного эксперимента: вопрос, сценарии, параметры, число прогонов, критерии сравнения и ожидаемые результаты. |
| [chapters/01_kompyuternoe_modelirovanie_i_julia/text/interpretation.md](chapters/01_kompyuternoe_modelirovanie_i_julia/text/interpretation.md) | файл, 90 Б | 2026-09-30 | Биологическая интерпретация траекторий, таблиц и рисунков. |
| [chapters/01_kompyuternoe_modelirovanie_i_julia/text/limitations.md](chapters/01_kompyuternoe_modelirovanie_i_julia/text/limitations.md) | файл, 95 Б | 2026-09-30 | Ограничения модели: биологические, математические, численные, связанные с данными и клинические. |
| [chapters/01_kompyuternoe_modelirovanie_i_julia/teaching](chapters/01_kompyuternoe_modelirovanie_i_julia/teaching/) | папка, 6 файлов, 667 Б | 2026-09-30 | Методические материалы для преподавателя и студентов. |
| [chapters/01_kompyuternoe_modelirovanie_i_julia/teaching/model_inventory.md](chapters/01_kompyuternoe_modelirovanie_i_julia/teaching/model_inventory.md) | файл, 145 Б | 2026-09-30 | Реестр моделей главы: тип, переменные, параметры, вопрос, ограничения, файлы реализации. |
| [chapters/01_kompyuternoe_modelirovanie_i_julia/teaching/glossary.md](chapters/01_kompyuternoe_modelirovanie_i_julia/teaching/glossary.md) | файл, 114 Б | 2026-09-30 | Глоссарий: биологические и медицинские, математические, программно-вычислительные термины. |
| [chapters/01_kompyuternoe_modelirovanie_i_julia/teaching/terminology_table.md](chapters/01_kompyuternoe_modelirovanie_i_julia/teaching/terminology_table.md) | файл, 126 Б | 2026-09-30 | Таблица терминов и обозначений: термин, определение, единицы, английский эквивалент, где используется. |
| [chapters/01_kompyuternoe_modelirovanie_i_julia/teaching/assignments.md](chapters/01_kompyuternoe_modelirovanie_i_julia/teaching/assignments.md) | файл, 61 Б | 2026-09-30 | Задания трёх уровней: базовый, средний, продвинутый. |
| [chapters/01_kompyuternoe_modelirovanie_i_julia/teaching/instructor_notes.md](chapters/01_kompyuternoe_modelirovanie_i_julia/teaching/instructor_notes.md) | файл, 93 Б | 2026-09-30 | Заметки преподавателя: цели обучения, последовательность изложения, типичные ошибки, оценивание. |
| [chapters/01_kompyuternoe_modelirovanie_i_julia/teaching/questions.md](chapters/01_kompyuternoe_modelirovanie_i_julia/teaching/questions.md) | файл, 128 Б | 2026-09-30 | Контрольные вопросы к главе. |
| [chapters/01_kompyuternoe_modelirovanie_i_julia/references](chapters/01_kompyuternoe_modelirovanie_i_julia/references/) | папка, 5 файлов, 298 Б | 2026-09-30 | Источники главы и реестр цитирования. |
| [chapters/01_kompyuternoe_modelirovanie_i_julia/references/bibliography.bib](chapters/01_kompyuternoe_modelirovanie_i_julia/references/bibliography.bib) | файл, 24 Б | 2026-09-30 | BibTeX-база для цитирования в Quarto. |
| [chapters/01_kompyuternoe_modelirovanie_i_julia/references/source_registry.csv](chapters/01_kompyuternoe_modelirovanie_i_julia/references/source_registry.csv) | файл, 81 Б | 2026-09-30 | Реестр источников: утверждение, где используется, тип источника, библиографическая ссылка, DOI или URL, дата доступа, статус проверки. |
| [chapters/01_kompyuternoe_modelirovanie_i_julia/references/references_main.md](chapters/01_kompyuternoe_modelirovanie_i_julia/references/references_main.md) | файл, 19 Б | 2026-09-30 | Основные источники главы. |
| [chapters/01_kompyuternoe_modelirovanie_i_julia/references/references_optional.md](chapters/01_kompyuternoe_modelirovanie_i_julia/references/references_optional.md) | файл, 23 Б | 2026-09-30 | Дополнительная литература для углублённого изучения. |
| [chapters/01_kompyuternoe_modelirovanie_i_julia/references/online_resources.md](chapters/01_kompyuternoe_modelirovanie_i_julia/references/online_resources.md) | файл, 151 Б | 2026-09-30 | Таблица онлайн-ресурсов и видео: ресурс, тип, автор или организация, URL, дата доступа, назначение. |

## Глава 01 — данные, результаты, ресурсы и иллюстрации

| Путь | Тип / размер | Изменён | Комментарий |
|---|---|---|---|
| [chapters/01_kompyuternoe_modelirovanie_i_julia/data](chapters/01_kompyuternoe_modelirovanie_i_julia/data/) | папка, 4 файла, 167 Б | 2026-09-30 | Данные главы. Пока пустая структура с README-заглушками. |
| [chapters/01_kompyuternoe_modelirovanie_i_julia/data/raw](chapters/01_kompyuternoe_modelirovanie_i_julia/data/raw/) | папка, 1 файл, 75 Б | 2026-09-30 | Исходные (сырые) данные. Вручную не изменяются — только добавление новых выгрузок. |
| [chapters/01_kompyuternoe_modelirovanie_i_julia/data/processed](chapters/01_kompyuternoe_modelirovanie_i_julia/data/processed/) | папка, 1 файл, 67 Б | 2026-09-30 | Данные после обработки скриптами главы. |
| [chapters/01_kompyuternoe_modelirovanie_i_julia/data/metadata](chapters/01_kompyuternoe_modelirovanie_i_julia/data/metadata/) | папка, 1 файл, 17 Б | 2026-09-30 | Описания данных: происхождение, единицы измерения, лицензия, ограничения. |
| [chapters/01_kompyuternoe_modelirovanie_i_julia/figures](chapters/01_kompyuternoe_modelirovanie_i_julia/figures/) | папка, 3 файла, 41 Б | 2026-09-30 | Итоговые рисунки главы. |
| [chapters/01_kompyuternoe_modelirovanie_i_julia/figures/svg](chapters/01_kompyuternoe_modelirovanie_i_julia/figures/svg/) | папка, 1 файл, 15 Б | 2026-09-30 | Векторные рисунки для сборки. Отслеживаются git. |
| [chapters/01_kompyuternoe_modelirovanie_i_julia/figures/png](chapters/01_kompyuternoe_modelirovanie_i_julia/figures/png/) | папка, 1 файл, 15 Б | 2026-09-30 | Растровые рисунки для веб-версии. Отслеживаются git. |
| [chapters/01_kompyuternoe_modelirovanie_i_julia/results](chapters/01_kompyuternoe_modelirovanie_i_julia/results/) | папка, 3 файла, 40 Б | 2026-09-30 | Результаты прогонов модели. |
| [chapters/01_kompyuternoe_modelirovanie_i_julia/results/tables](chapters/01_kompyuternoe_modelirovanie_i_julia/results/tables/) | папка, 1 файл, 17 Б | 2026-09-30 | Таблицы результатов (CSV, LaTeX). |
| [chapters/01_kompyuternoe_modelirovanie_i_julia/results/logs](chapters/01_kompyuternoe_modelirovanie_i_julia/results/logs/) | папка, 1 файл, 12 Б | 2026-09-30 | Журналы запусков. Содержимое игнорируется git, кроме README; здесь же появляется `startme.log`. |
| [chapters/01_kompyuternoe_modelirovanie_i_julia/resources](chapters/01_kompyuternoe_modelirovanie_i_julia/resources/) | папка, 6 файлов, 161 Б | 2026-09-30 | Библиотека учебных материалов главы. |
| [chapters/01_kompyuternoe_modelirovanie_i_julia/resources/books](chapters/01_kompyuternoe_modelirovanie_i_julia/resources/books/) | папка, 1 файл, 23 Б | 2026-09-30 | Книги и учебники. |
| [chapters/01_kompyuternoe_modelirovanie_i_julia/resources/papers](chapters/01_kompyuternoe_modelirovanie_i_julia/resources/papers/) | папка, 1 файл, 10 Б | 2026-09-30 | Научные статьи. |
| [chapters/01_kompyuternoe_modelirovanie_i_julia/resources/reading](chapters/01_kompyuternoe_modelirovanie_i_julia/resources/reading/) | папка, 1 файл, 88 Б | 2026-09-30 | Подборки для чтения. |
| [chapters/01_kompyuternoe_modelirovanie_i_julia/resources/videos](chapters/01_kompyuternoe_modelirovanie_i_julia/resources/videos/) | папка, 1 файл, 10 Б | 2026-09-30 | Видеоматериалы. |
| [chapters/01_kompyuternoe_modelirovanie_i_julia/resources/web](chapters/01_kompyuternoe_modelirovanie_i_julia/resources/web/) | папка, 1 файл, 17 Б | 2026-09-30 | Полезные веб-ресурсы. |
| [chapters/01_kompyuternoe_modelirovanie_i_julia/images](chapters/01_kompyuternoe_modelirovanie_i_julia/images/) | папка, 24 файла, 1,4 МБ | 2026-10-03 | Скриншоты для вставки в главу (`paste-1.png` … `paste-12.png`; самый крупный — `paste-8.png`, ~204 КБ). |

## Глава 02 — паспорт, текст и структура

| Путь | Тип / размер | Изменён | Комментарий |
|---|---|---|---|
| [chapters/02_prostye_modeli_osnovy_chislennykh_metodov](chapters/02_prostye_modeli_osnovy_chislennykh_metodov/) | папка, 69 файлов, 2,2 МБ | 2026-10-04 | Глава 02 «Простые модели. Основы численных методов»: текст главы, каркас скриптов и типовое дерево каталогов (text, julia, pluto, data, results, figures, resources, references, teaching). |
| [chapters/02_prostye_modeli_osnovy_chislennykh_metodov/_metadata.yaml](chapters/02_prostye_modeli_osnovy_chislennykh_metodov/_metadata.yaml) | файл, 3,2 КБ | 2026-10-04 | Паспорт главы 02 (ID, номер, название, статус draft, автор — ПсковГУ, дата) и настройки вывода Quarto для HTML, Typst/PDF и DOCX — те же, что в главе 01, но с исправленными реквизитами главы. |
| [chapters/02_prostye_modeli_osnovy_chislennykh_metodov/metadata.yaml](chapters/02_prostye_modeli_osnovy_chislennykh_metodov/metadata.yaml) | файл, 497 Б | 2026-10-04 | Служебный паспорт, который создаёт генератор `init_chapter_interactive_v2.py` (ID, номер, название, дата, комментарий). Частично дублирует `_metadata.yaml`. |
| [chapters/02_prostye_modeli_osnovy_chislennykh_metodov/chapter.qmd](chapters/02_prostye_modeli_osnovy_chislennykh_metodov/chapter.qmd) | файл, 51,6 КБ | 2026-10-04 | Главный содержательный исходник главы: введение, сквозные биомедицинские примеры (фармакокинетика, AUC, Михаэлис–Ментен), минимум Julia, бисекция/Ньютон/секущие, трапеции и Симпсон, численное дифференцирование, символьные методы, программа вычислительного эксперимента, интерпретация, ограничения, задания и ссылки на материалы. Править текст нужно прежде всего здесь. |
| [chapters/02_prostye_modeli_osnovy_chislennykh_metodov/chapter.md](chapters/02_prostye_modeli_osnovy_chislennykh_metodov/chapter.md) | файл, 8,4 КБ | 2026-10-04 | Шаблон Markdown-версии главы с YAML-фронтматтером и навигацией по разделам. |
| [chapters/02_prostye_modeli_osnovy_chislennykh_metodov/custom-reference.docx](chapters/02_prostye_modeli_osnovy_chislennykh_metodov/custom-reference.docx) | файл, 42,4 КБ | 2026-09-30 | Эталонный документ Word со стилями для DOCX-вывода (`reference-doc` в `_metadata.yaml`). |
| [chapters/02_prostye_modeli_osnovy_chislennykh_metodov/chapter.html](chapters/02_prostye_modeli_osnovy_chislennykh_metodov/chapter.html) | файл, 124,6 КБ | 2026-10-04 | Собранная HTML-версия главы. Генерируется Quarto, вручную не правится. |
| [chapters/02_prostye_modeli_osnovy_chislennykh_metodov/chapter_files](chapters/02_prostye_modeli_osnovy_chislennykh_metodov/chapter_files/) | папка, 12 файлов, 864,6 КБ | 2026-10-04 | Ресурсы HTML-рендера: Bootstrap, quarto-html, tippy, tabsets. Полностью генерируется, править не нужно. |
| [chapters/02_prostye_modeli_osnovy_chislennykh_metodov/StartMe.jl](chapters/02_prostye_modeli_osnovy_chislennykh_metodov/StartMe.jl) | файл, 3,9 КБ | 2026-10-04 | Центральный узел главы: ищет корень проекта, объявляет константы `DIR_*`, создаёт каталоги, пишет журнал прогона и печатает конфигурацию. |
| [chapters/02_prostye_modeli_osnovy_chislennykh_metodov/StartMe copy.jl](<chapters/02_prostye_modeli_osnovy_chislennykh_metodov/StartMe copy.jl>) | файл, 3,7 КБ | 2026-09-30 | Копия `StartMe.jl`, оставшаяся после копирования структуры главы 01. Рабочим входом не является, кандидат на удаление. |
| [chapters/02_prostye_modeli_osnovy_chislennykh_metodov/julia](chapters/02_prostye_modeli_osnovy_chislennykh_metodov/julia/) | папка, 6 файлов, 30,9 КБ | 2026-10-04 | Каркас скриптов главы (main.jl, run_experiments.jl, make_figures.jl, tests/runtests.jl). Пока заглушки вокруг StartMe.jl: логика расчётов ещё не реализована. |
| [chapters/02_prostye_modeli_osnovy_chislennykh_metodov/julia/bisection_demo.jl](chapters/02_prostye_modeli_osnovy_chislennykh_metodov/julia/bisection_demo.jl) | файл, 14,4 КБ | 2026-10-04 | Пошаговая демонстрация метода бисекции (уравнение C0·exp(−kt) − C_МТК = 0): печатает таблицу шагов «старт, первые 4 шага, финиш», пишет полный журнал всех итераций в `results/tables/bisection_steps.csv` и строит рисунок из четырёх панелей (функция и корень, «лестница» отрезков [a; b], сходимость по аргументу, крупный план финиша) в `figures/svg` и `figures/png`. |
| [chapters/02_prostye_modeli_osnovy_chislennykh_metodov/julia/newton_demo.jl](chapters/02_prostye_modeli_osnovy_chislennykh_metodov/julia/newton_demo.jl) | файл, 16,1 КБ | 2026-10-04 | Пошаговая демонстрация метода Ньютона для того же уравнения: печатает таблицу шагов «старт, первые 4 шага, финиш» (xₙ, f(xₙ), f′(xₙ), xₙ₊₁, Δx), пишет журнал в `results/tables/newton_steps.csv` и строит рисунок из четырёх панелей (касательные метода, переходы xₙ → xₙ₊₁, сходимость с проверкой квадратичного закона, крупный план финиша) в `figures/svg` и `figures/png`. |
| [chapters/02_prostye_modeli_osnovy_chislennykh_metodov/pluto](chapters/02_prostye_modeli_osnovy_chislennykh_metodov/pluto/) | папка, 3 файла, 244 Б | 2026-10-04 | Каркас блокнотов Pluto (01_main_model.jl, 02_experiment.jl) и README с напоминанием о корневом Julia-окружении. |
| [chapters/02_prostye_modeli_osnovy_chislennykh_metodov/text](chapters/02_prostye_modeli_osnovy_chislennykh_metodov/text/) | папка, 5 файлов, 686 Б | 2026-10-04 | Смысловые блоки главы (шаблоны с одними заголовками). Содержательная часть пока живёт в `chapter.qmd`. |
| [chapters/02_prostye_modeli_osnovy_chislennykh_metodov/data](chapters/02_prostye_modeli_osnovy_chislennykh_metodov/data/) | папка, 4 файла, 167 Б | 2026-10-04 | Типовая структура данных с README-заглушками: raw, processed, metadata. |
| [chapters/02_prostye_modeli_osnovy_chislennykh_metodov/results](chapters/02_prostye_modeli_osnovy_chislennykh_metodov/results/) | папка, 6 файлов, 3,6 КБ | 2026-10-04 | Каталоги для таблиц результатов и журналов прогонов. |
| [chapters/02_prostye_modeli_osnovy_chislennykh_metodov/figures](chapters/02_prostye_modeli_osnovy_chislennykh_metodov/figures/) | папка, 7 файлов, 1,1 МБ | 2026-10-04 | Каталоги для рисунков SVG и PNG. |
| [chapters/02_prostye_modeli_osnovy_chislennykh_metodov/resources](chapters/02_prostye_modeli_osnovy_chislennykh_metodov/resources/) | папка, 6 файлов, 161 Б | 2026-10-04 | Библиотека учебных материалов главы: books, papers, reading, videos, web. |
| [chapters/02_prostye_modeli_osnovy_chislennykh_metodov/references](chapters/02_prostye_modeli_osnovy_chislennykh_metodov/references/) | папка, 5 файлов, 298 Б | 2026-10-04 | Источники главы: bibliography.bib, references_main.md, references_optional.md, online_resources.md, source_registry.csv. |
| [chapters/02_prostye_modeli_osnovy_chislennykh_metodov/teaching](chapters/02_prostye_modeli_osnovy_chislennykh_metodov/teaching/) | папка, 6 файлов, 667 Б | 2026-10-04 | Методические материалы: assignments, questions, instructor_notes, terminology_table, model_inventory, glossary. |

## Общие правила и маски

| Путь | Тип / размер | Изменён | Комментарий |
|---|---|---|---|
| `*/README.md` | 37 файлов, 5,5 КБ | 2026-10-04 | Служебные README-указатели внутри папок структуры: напоминают назначение каталога и созданы генератором глав. Описания конкретных README — в соответствующих разделах выше. |

## Не описано в реестре

Эти пути существуют в дереве, но для них нет записи в `tools/file_map_registry.md`. Добавьте строку и перезапустите генератор:

- `chapters/01_kompyuternoe_modelirovanie_i_julia/pluto/notebook01.jl`
