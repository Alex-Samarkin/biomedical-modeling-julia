# Реестр комментариев для карты проекта

Этот файл — **единственное место, где правятся текстовые пояснения**. Скрипт
`tools/update_file_map.py` пересчитывает структуру, размеры и даты автоматически,
а описания берёт отсюда, поэтому после добавления новой папки или файла достаточно
дописать одну строку в нужный раздел и запустить скрипт ещё раз.

## Формат

Каждая запись — это одна строка вида «путь, затем разделитель из двух двоеточий
с пробелами, затем комментарий». Пример записи:

```text
- путь/к/файлу.md :: Что это и зачем нужно.
```

- `## Название` — заголовок раздела карты (порядок разделов = порядок в `FILES.md`).
- Путь указывается относительно корня репозитория, разделитель — прямой слеш `/`.
- Путь, оканчивающийся на `/`, — папка: в карте показывается число файлов и их объём.
- Символы `*` и `?` — маска: в карте показывается число совпадений (например `*/README.md`).
- Префикс `!` перед путём папки — «непрозрачная» папка: её содержимое считается
  описанным и не попадает в раздел «Не описано в реестре» (нужно для генерируемых
  и служебных каталогов).
- Строки без разделителя игнорируются.

## Корень репозитория

- Project.toml :: Единое Julia-окружение всего проекта: DifferentialEquations и OrdinaryDiffEq, ModelingToolkit, DataFrames и CSV, Distributions и StatsBase, Plots вместе с CairoMakie, Pluto, IJulia, JLD2, JSON, XLSX, Test. Главы активируют именно этот файл (`julia_environment: ../../Project.toml`).
- Manifest.toml :: Зафиксированные версии всех зависимостей (~152 КБ). Осознанно хранится в git — это основа воспроизводимости расчётов.
- SetupProject.jl :: Первичная установка окружения: `Pkg.activate(".")` и `Pkg.add([...])` того же набора пакетов, что объявлен в Project.toml.
- init_chapter_interactive_v2.py :: Интерактивный генератор новой главы (433 строки): спрашивает номер и название, транслитерирует их в ASCII-slug, создаёт дерево каталогов, StartMe.jl, chapter.md, _metadata.yaml и все шаблоны через `files_for_chapter()`.
- pyproject.toml :: Python-обёртка (uv) вокруг этого генератора: пакет `biomedical-modeling-julia`, точка входа `biomedical-modeling-julia`, сборка через `uv_build`.
- uv.lock :: Лок-файл uv. Внешних Python-зависимостей нет — только сам пакет проекта в editable-режиме.
- .python-version :: Требуемая версия Python для uv (3.14).
- .gitignore :: Политика хранения: Project.toml и Manifest.toml отслеживаются; отслеживаются результаты `*.csv`, `*.svg`, `*.png`, `*.jld2`; игнорируются `*.xlsx`, `*.parquet`, `*.h5`, `*.mat`, медиафайлы, содержимое `results/logs/` и все кэши.
- README.md :: Главная страница репозитория: назначение проекта, что уже готово, команды запуска и порядок обслуживания карты проекта (блок структуры обновляется скриптом).
- FILES.md :: Эта карта проекта: полный список ключевых файлов и папок с комментариями. Файл генерируется, править его вручную не нужно — правьте `tools/file_map_registry.md`.
- AGENTS.md :: Постоянная память проекта для ИИ-ассистента: роль (инженер, к.т.н., математическое моделирование в биомедицине), аудитория и стиль текстов, требования к коду и комментариям, технологический стек, правила работы с артефактами карты проекта.
- УЧАСТНИКИ ПОРЯДОК РАБОТЫ.docx :: Организационный документ: состав участников проекта и регламент совместной работы.
- src/ :: Исходники Python-пакета-обёртки.
- src/biomedical_modeling_julia/ :: Пакет `biomedical_modeling_julia`, указанный как точка входа в pyproject.toml.
- src/biomedical_modeling_julia/__init__.py :: Заглушка пакета: функция `main()` печатает приветствие, нужна только для точки входа из pyproject.toml.
- tools/ :: Служебные скрипты сопровождения репозитория: реестр комментариев, генератор карты проекта и инструкция по их запуску.
- tools/README.md :: Инструкция по обслуживанию карты: команды запуска, формат реестра, режим проверки и плановый интервал обновления.
- tools/update_file_map.py :: Генератор карты проекта: читает реестр, обходит дерево репозитория, считает размеры и даты, пишет FILES.md и блок структуры в README.md. Зависимостей нет, только стандартная библиотека Python.
- tools/file_map_registry.md :: Этот реестр: пути и текстовые пояснения, которые попадают в карту.
- chapters/ :: Все главы пособия. Одна папка — одна глава; сейчас создана только глава 01.

## Глава 01 — паспорт, сборка и артефакты

- chapters/01_kompyuternoe_modelirovanie_i_julia/ :: Глава 01 «Компьютерное моделирование и Julia»: исходники текста, код, ноутбуки, данные, результаты и методические материалы.
- chapters/01_kompyuternoe_modelirovanie_i_julia/README.md :: Краткая карточка главы: название, тема и ссылка на основной файл chapter.md.
- chapters/01_kompyuternoe_modelirovanie_i_julia/_metadata.yaml :: Паспорт главы (номер, ID, статус draft, автор — ПсковГУ, дата) и настройки вывода Quarto для трёх форматов: HTML (тема easy, выключка по ширине), Typst/PDF (A4, Calibri, кастомные заголовки и колонтитул) и DOCX.
- chapters/01_kompyuternoe_modelirovanie_i_julia/chapter.qmd :: Главный содержательный исходник главы (438 строк, движок jupyter): введение, зачем моделирование медикам, необходимый минимум математики, обзор средств моделирования. Править текст нужно прежде всего здесь.
- chapters/01_kompyuternoe_modelirovanie_i_julia/chapter.md :: Markdown-версия главы с YAML-фронтматтером и навигацией по разделам. Метаданные дублируют `_metadata.yaml` — при правке следите, чтобы они не разошлись.
- chapters/01_kompyuternoe_modelirovanie_i_julia/chapter.html :: Собранная HTML-версия главы. Генерируется Quarto, вручную не правится.
- chapters/01_kompyuternoe_modelirovanie_i_julia/chapter.pdf :: Собранный PDF через Typst. Генерируется Quarto, вручную не правится.
- chapters/01_kompyuternoe_modelirovanie_i_julia/chapter.docx :: Собранный Word-документ. Генерируется Quarto, вручную не правится.
- chapters/01_kompyuternoe_modelirovanie_i_julia/custom-reference.docx :: Эталонный документ Word со стилями для DOCX-вывода (`reference-doc` в `_metadata.yaml`).
- !chapters/01_kompyuternoe_modelirovanie_i_julia/chapter_files/ :: Ресурсы HTML-рендера: Bootstrap, quarto-html, tippy, tabsets (~1,4 МБ). Полностью генерируется, править не нужно.
- !chapters/01_kompyuternoe_modelirovanie_i_julia/.quarto/ :: Системный кэш Quarto, в том числе список доступных шрифтов для Typst.
- chapters/01_kompyuternoe_modelirovanie_i_julia/sample1.md :: Пример презентации в формате Marp — по теме диодов и электроники, то есть не по теме пособия. Кандидат на удаление или замену на биомедицинский пример.
- chapters/01_kompyuternoe_modelirovanie_i_julia/sample1.pdf :: Собранный PDF той же презентации.

## Глава 01 — код и вычисления

- chapters/01_kompyuternoe_modelirovanie_i_julia/StartMe.jl :: Центральный узел главы: ищет корень проекта по паре Project.toml + Manifest.toml, объявляет константы `DIR_*` (text, julia, pluto, data/raw, data/processed, data/metadata, results/tables, results/logs, figures/svg, figures/png, resources, references, teaching), создаёт каталоги, пишет журнал `results/logs/startme.log` и печатает конфигурацию.
- chapters/01_kompyuternoe_modelirovanie_i_julia/julia/ :: Скрипты главы. Запускаются из корня репозитория с ключом `--project=.`.
- chapters/01_kompyuternoe_modelirovanie_i_julia/julia/main.jl :: Заявленная точка входа главы. Пока заглушка: подключает StartMe.jl.
- chapters/01_kompyuternoe_modelirovanie_i_julia/julia/run_experiments.jl :: Сценарии вычислительного эксперимента. Пока заглушка вокруг StartMe.jl — здесь должна появиться логика прогонов и сохранения таблиц.
- chapters/01_kompyuternoe_modelirovanie_i_julia/julia/make_figures.jl :: Генерация рисунков SVG и PNG для главы. Пока заглушка вокруг StartMe.jl.
- chapters/01_kompyuternoe_modelirovanie_i_julia/julia/sample1.jl :: Учебный пример построения фигуры Лиссажу на Plots (backend GR) — образец оформления кода для главы.
- chapters/01_kompyuternoe_modelirovanie_i_julia/julia/tests/ :: Тесты главы.
- chapters/01_kompyuternoe_modelirovanie_i_julia/julia/tests/runtests.jl :: Smoke-тест: после запуска StartMe.jl проверяет существование каталогов `DIR_RESULTS`, `DIR_FIGURES_SVG`, `DIR_FIGURES_PNG`.
- chapters/01_kompyuternoe_modelirovanie_i_julia/pluto/ :: Интерактивные ноутбуки Pluto главы. Работают в корневом Julia-окружении репозитория.
- chapters/01_kompyuternoe_modelirovanie_i_julia/pluto/README.md :: Напоминание, что ноутбуки используют корневое окружение.
- chapters/01_kompyuternoe_modelirovanie_i_julia/pluto/01_main_model.jl :: Pluto-ноутбук с основной учебной моделью (каркас, формат v0.20.0).
- chapters/01_kompyuternoe_modelirovanie_i_julia/pluto/02_experiment.jl :: Pluto-ноутбук вычислительного эксперимента (каркас).

## Глава 01 — текст, методика и источники

- chapters/01_kompyuternoe_modelirovanie_i_julia/text/ :: Смысловые блоки главы. Сейчас это шаблоны с одними заголовками — содержательная часть пока живёт в `chapter.qmd`.
- chapters/01_kompyuternoe_modelirovanie_i_julia/text/academic_note.md :: Академическая справка: тема, объект и предмет моделирования, научно-методическая проблема, место главы в книге.
- chapters/01_kompyuternoe_modelirovanie_i_julia/text/mathematical_model.md :: Рабочая постановка модели: переменные, параметры, единицы измерения, начальные условия, уравнения и свойства модели.
- chapters/01_kompyuternoe_modelirovanie_i_julia/text/computational_experiment.md :: Описание вычислительного эксперимента: вопрос, сценарии, параметры, число прогонов, критерии сравнения и ожидаемые результаты.
- chapters/01_kompyuternoe_modelirovanie_i_julia/text/interpretation.md :: Биологическая интерпретация траекторий, таблиц и рисунков.
- chapters/01_kompyuternoe_modelirovanie_i_julia/text/limitations.md :: Ограничения модели: биологические, математические, численные, связанные с данными и клинические.
- chapters/01_kompyuternoe_modelirovanie_i_julia/teaching/ :: Методические материалы для преподавателя и студентов.
- chapters/01_kompyuternoe_modelirovanie_i_julia/teaching/model_inventory.md :: Реестр моделей главы: тип, переменные, параметры, вопрос, ограничения, файлы реализации.
- chapters/01_kompyuternoe_modelirovanie_i_julia/teaching/glossary.md :: Глоссарий: биологические и медицинские, математические, программно-вычислительные термины.
- chapters/01_kompyuternoe_modelirovanie_i_julia/teaching/terminology_table.md :: Таблица терминов и обозначений: термин, определение, единицы, английский эквивалент, где используется.
- chapters/01_kompyuternoe_modelirovanie_i_julia/teaching/assignments.md :: Задания трёх уровней: базовый, средний, продвинутый.
- chapters/01_kompyuternoe_modelirovanie_i_julia/teaching/instructor_notes.md :: Заметки преподавателя: цели обучения, последовательность изложения, типичные ошибки, оценивание.
- chapters/01_kompyuternoe_modelirovanie_i_julia/teaching/questions.md :: Контрольные вопросы к главе.
- chapters/01_kompyuternoe_modelirovanie_i_julia/references/ :: Источники главы и реестр цитирования.
- chapters/01_kompyuternoe_modelirovanie_i_julia/references/bibliography.bib :: BibTeX-база для цитирования в Quarto.
- chapters/01_kompyuternoe_modelirovanie_i_julia/references/source_registry.csv :: Реестр источников: утверждение, где используется, тип источника, библиографическая ссылка, DOI или URL, дата доступа, статус проверки.
- chapters/01_kompyuternoe_modelirovanie_i_julia/references/references_main.md :: Основные источники главы.
- chapters/01_kompyuternoe_modelirovanie_i_julia/references/references_optional.md :: Дополнительная литература для углублённого изучения.
- chapters/01_kompyuternoe_modelirovanie_i_julia/references/online_resources.md :: Таблица онлайн-ресурсов и видео: ресурс, тип, автор или организация, URL, дата доступа, назначение.

## Глава 01 — данные, результаты, ресурсы и иллюстрации

- chapters/01_kompyuternoe_modelirovanie_i_julia/data/ :: Данные главы. Пока пустая структура с README-заглушками.
- chapters/01_kompyuternoe_modelirovanie_i_julia/data/raw/ :: Исходные (сырые) данные. Вручную не изменяются — только добавление новых выгрузок.
- chapters/01_kompyuternoe_modelirovanie_i_julia/data/processed/ :: Данные после обработки скриптами главы.
- chapters/01_kompyuternoe_modelirovanie_i_julia/data/metadata/ :: Описания данных: происхождение, единицы измерения, лицензия, ограничения.
- chapters/01_kompyuternoe_modelirovanie_i_julia/figures/ :: Итоговые рисунки главы.
- chapters/01_kompyuternoe_modelirovanie_i_julia/figures/svg/ :: Векторные рисунки для сборки. Отслеживаются git.
- chapters/01_kompyuternoe_modelirovanie_i_julia/figures/png/ :: Растровые рисунки для веб-версии. Отслеживаются git.
- chapters/01_kompyuternoe_modelirovanie_i_julia/results/ :: Результаты прогонов модели.
- chapters/01_kompyuternoe_modelirovanie_i_julia/results/tables/ :: Таблицы результатов (CSV, LaTeX).
- chapters/01_kompyuternoe_modelirovanie_i_julia/results/logs/ :: Журналы запусков. Содержимое игнорируется git, кроме README; здесь же появляется `startme.log`.
- chapters/01_kompyuternoe_modelirovanie_i_julia/resources/ :: Библиотека учебных материалов главы.
- chapters/01_kompyuternoe_modelirovanie_i_julia/resources/books/ :: Книги и учебники.
- chapters/01_kompyuternoe_modelirovanie_i_julia/resources/papers/ :: Научные статьи.
- chapters/01_kompyuternoe_modelirovanie_i_julia/resources/reading/ :: Подборки для чтения.
- chapters/01_kompyuternoe_modelirovanie_i_julia/resources/videos/ :: Видеоматериалы.
- chapters/01_kompyuternoe_modelirovanie_i_julia/resources/web/ :: Полезные веб-ресурсы.
- !chapters/01_kompyuternoe_modelirovanie_i_julia/images/ :: Скриншоты для вставки в главу (`paste-1.png` … `paste-12.png`; самый крупный — `paste-8.png`, ~204 КБ).

## Общие правила и маски

- */README.md :: Служебные README-указатели внутри папок структуры: напоминают назначение каталога и созданы генератором глав. Описания конкретных README — в соответствующих разделах выше.
