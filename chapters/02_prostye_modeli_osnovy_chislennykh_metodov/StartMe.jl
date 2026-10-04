"""
StartMe.jl — конфигурация главы 02: Простые модели. Основы численных методов

Chapter ID: 02_prostye_modeli_osnovy_chislennykh_metodov
Created: 2026-10-04
Comment: Рассматриваются приемы работы в Julia, основы решения уравнений, интегрирования и дифференцирования численными и символьными методами

Запуск из корня репозитория:
    julia --project=. chapters/02_prostye_modeli_osnovy_chislennykh_metodov/StartMe.jl

StartMe.jl расположен в корне главы и является единым входом для настройки
путей, каталогов результатов и базовой конфигурации главы.
"""

using Dates

const CHAPTER_NUMBER = "02"
const CHAPTER_TITLE = "Простые модели. Основы численных методов"
const CHAPTER_ID = "02_prostye_modeli_osnovy_chislennykh_metodov"

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
