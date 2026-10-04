"""
bisection_demo.jl — пошаговая демонстрация метода бисекции.

Скрипт решает фармакокинетическое уравнение

    f(t) = C0 · exp(−k·t) − C_МТК = 0

методом деления отрезка пополам и показывает работу метода:

  * таблицу шагов на экране (старт, первые четыре шага, финиш);
  * полный журнал всех шагов в results/tables/bisection_steps.csv;
  * рисунок из четырёх панелей в figures/svg и figures/png:
      A — график функции и середины первых шагов;
      B — «лестница» отрезков [a; b] по шагам;
      C — сходимость по аргументу (ширина отрезка и ошибка в лог. шкале);
      D — крупный план окрестности корня: последние шаги и финиш.

Запуск из корня репозитория:

    julia --project=. chapters/02_prostye_modeli_osnovy_chislennykh_metodov/julia/bisection_demo.jl
"""

# Стандартный вход главы: корень проекта, каталоги DIR_* и журнал прогона.
include(joinpath(@__DIR__, "..", "StartMe.jl"))

using CSV
using Plots

# --------------------------------------------------------------------------
# 1. Модель и постановка задачи
# --------------------------------------------------------------------------

const C0_MG_L = 20.0        # начальная концентрация препарата, мг/л
const K_ELIM_1H = 0.15      # константа элиминации, 1/ч
const MTC_MG_L = 2.0        # минимальная терапевтическая концентрация, мг/л

const A0_H = 0.0            # левый конец отрезка локализации корня, ч
const B0_H = 48.0           # правый конец отрезка локализации корня, ч
const XTOL_H = 1e-6         # допуск по аргументу, ч

const N_FIRST_SHOWN = 4     # сколько первых шагов показываем отдельно

"Концентрация препарата в момент времени t (ч), мг/л."
concentration(t) = C0_MG_L * exp(-K_ELIM_1H * t)

"Невязка задачи: отклонение концентрации от терапевтического порога, мг/л."
residual(t) = concentration(t) - MTC_MG_L

"Точное решение уравнения f(t) = 0, ч (нужно для контроля метода)."
const T_EXACT_H = log(C0_MG_L / MTC_MG_L) / K_ELIM_1H

# --------------------------------------------------------------------------
# 2. Метод бисекции с журналом шагов
# --------------------------------------------------------------------------

"""
Один шаг метода: текущий отрезок [a; b], его середина m и невязка f(m).

Для «стартовой» записи (iter = 0) середина ещё не вычислена, поэтому m и fm
равны NaN — так видно, что это исходная постановка, а не шаг метода.
"""
struct BisectionStep
    iter::Int
    a::Float64
    b::Float64
    m::Float64
    fm::Float64
    width::Float64
end

"""
    bisect_logged(f, a0, b0; xtol, max_iter) -> (root, steps)

Метод бисекции для непрерывной функции f на отрезке [a0; b0].

Возвращает найденный корень и вектор записей BisectionStep: первая запись —
стартовый отрезок, далее по одной записи на каждую итерацию (в записи шага
хранится отрезок, который был использован для вычисления середины).
"""
function bisect_logged(f, a0::Float64, b0::Float64; xtol::Float64 = 1e-6, max_iter::Int = 200)
    fa, fb = f(a0), f(b0)
    fa * fb > 0 && error("На концах отрезка функция одного знака: корень не локализован.")

    steps = BisectionStep[BisectionStep(0, a0, b0, NaN, NaN, b0 - a0)]
    a, b = a0, b0

    for iter in 1:max_iter
        m = (a + b) / 2          # середина текущего отрезка
        fm = f(m)
        push!(steps, BisectionStep(iter, a, b, m, fm, b - a))

        (b - a) < xtol && return m, steps   # достигнут допуск по аргументу

        if fa * fm < 0           # знак сменился на левой половине
            b, fb = m, fm
        else                     # корень в правой половине
            a, fa = m, fm
        end
    end

    return (a + b) / 2, steps
end

# --------------------------------------------------------------------------
# 3. Вывод шагов на экран
# --------------------------------------------------------------------------

"Число для таблицы: NaN показываем прочерком (у стартовой записи нет середины)."
function fmt_value(x::Float64, digits::Int = 6)
    isnan(x) && return "—"
    return string(round(x, digits = digits))
end

"Напечатать выбранные шаги в виде таблицы с подписью «старт» и «финиш»."
function print_steps(steps::Vector{BisectionStep}, selected::Vector{Int}, last_iter::Int)
    header = ("шаг", "a, ч", "b, ч", "m, ч", "f(m), мг/л", "ширина, ч")
    widths = (8, 12, 12, 12, 14, 12)
    println(join(lpad.(header, widths), " "))
    println("-"^74)
    for st in steps
        st.iter in selected || continue
        label = st.iter == 0 ? "старт" : (st.iter == last_iter ? "финиш" : string(st.iter))
        # Ширину печатаем с большим числом знаков: на финише она порядка 1e-7 ч.
        row = (label, fmt_value(st.a), fmt_value(st.b), fmt_value(st.m),
               fmt_value(st.fm), fmt_value(st.width, 8))
        println(join(lpad.(row, widths), " "))
    end
end

# --------------------------------------------------------------------------
# 4. Запуск метода
# --------------------------------------------------------------------------

t_root, steps = bisect_logged(residual, A0_H, B0_H; xtol = XTOL_H)
last_iter = steps[end].iter

# Показываем старт, первые N_FIRST_SHOWN шагов и финиш.
selected = vcat(0, collect(1:N_FIRST_SHOWN), last_iter)

println("\nМетод бисекции: f(t) = C(t) − C_МТК, отрезок [$(A0_H); $(B0_H)] ч, допуск $(XTOL_H) ч")
print_steps(steps, selected, last_iter)

println("\nНайдено:  t = ", round(t_root, digits = 9), " ч за ", last_iter, " итераций")
println("Точно:    t = ", round(T_EXACT_H, digits = 9), " ч (формула ln(C0/C_МТК)/k)")
println("Ошибка по аргументу: ", abs(t_root - T_EXACT_H), " ч")
println("Проверка: C(t) = ", round(concentration(t_root), digits = 9),
        " мг/л вместо ", MTC_MG_L, " мг/л")

# --------------------------------------------------------------------------
# 5. Полный журнал шагов в CSV
# --------------------------------------------------------------------------

csv_path = joinpath(DIR_RESULTS_TABLES, "bisection_steps.csv")
CSV.write(csv_path, (
    step = [st.iter for st in steps],
    a_h = [st.a for st in steps],
    b_h = [st.b for st in steps],
    m_h = [st.m for st in steps],
    f_m_mg_l = [st.fm for st in steps],
    width_h = [st.width for st in steps],
))
println("\nЖурнал шагов: ", csv_path)

# --------------------------------------------------------------------------
# 6. Рисунок: четыре панели
# --------------------------------------------------------------------------

t_curve = range(A0_H, B0_H; length = 500)          # кривая невязки на всём отрезке
first_steps = [st for st in steps if 1 <= st.iter <= N_FIRST_SHOWN]
tail_steps = [st for st in steps if st.iter > last_iter - 5]   # последние пять шагов

# Панель A: функция, корень и середины первых шагов.
panel_a = plot(t_curve, residual.(t_curve);
    label = "f(t) = C(t) − C_МТК",
    xlabel = "время t, ч", ylabel = "f(t), мг/л",
    title = "A. Уравнение и первые шаги",
    linewidth = 2, color = :navy, legend = :topright)
hline!(panel_a, [0.0]; color = :black, linestyle = :dash, linewidth = 1, label = "нулевой уровень")
vline!(panel_a, [T_EXACT_H]; color = :green, linestyle = :dot, linewidth = 2, label = "точный корень t*")
scatter!(panel_a, [st.m for st in first_steps], [st.fm for st in first_steps];
    color = :red, markersize = 6, markerstrokewidth = 0, label = "середины шагов 1–$(N_FIRST_SHOWN)")
for st in first_steps
    # Подпись уводим на свободную сторону: выше точки при f(m) < 0 и ниже при f(m) > 0.
    dy = st.fm < 0 ? 2.2 : -1.2
    annotate!(panel_a, st.m, st.fm + dy, text("шаг $(st.iter)", 8, :red))
end
plot(panel_a, [A0_H, B0_H], [0.0, 0.0]; color = :black, linestyle = :dash, linewidth = 1, label = "")

# Панель B: «лестница» отрезков — наглядно видно, как отрезок стягивается к корню.
ladder = vcat(steps[1:1], first_steps, steps[end:end])       # старт, шаги 1–4, финиш
ladder_y = collect(0:-1:-(length(ladder) - 1))
ladder_labels = [st.iter == 0 ? "старт" : (st.iter == last_iter ? "финиш" : "шаг $(st.iter)")
                 for st in ladder]
x_hi = 26.0                                                  # окно по времени, ч
panel_b = plot(; xlabel = "время t, ч", ylabel = "", yticks = (ladder_y, ladder_labels),
    title = "B. Отрезки [a; b] (окно 0–$(Int(x_hi)) ч)", legend = :bottomleft,
    ylims = (minimum(ladder_y) - 0.7, maximum(ladder_y) + 0.7), xlims = (A0_H, x_hi))
for (k, st) in enumerate(ladder)
    y = ladder_y[k]
    plot!(panel_b, [clamp(st.a, A0_H, x_hi), clamp(st.b, A0_H, x_hi)], [y, y];
        color = :steelblue, linewidth = 7, label = k == 1 ? "отрезок [a; b]" : "")
    scatter!(panel_b, [clamp(st.m, A0_H, x_hi)], [y];
        color = :red, markersize = 4, label = k == 1 ? "середина m" : "")
end
vline!(panel_b, [T_EXACT_H]; color = :green, linestyle = :dot, linewidth = 2, label = "точный корень t*")
plot(panel_b, [A0_H, B0_H], [0.0, 0.0]; color = :black, linestyle = :dash, linewidth = 1, label = "")

# Панель C: сходимость — ширина отрезка и фактическая ошибка (логарифмическая шкала).
iter_all = [st.iter for st in steps if st.iter > 0]
width_all = [st.width for st in steps if st.iter > 0]
# Точное совпадение даёт нулевую ошибку, которую нельзя показать в лог. шкале.
error_all = [e == 0.0 ? NaN : e for e in (abs(st.m - T_EXACT_H) for st in steps if st.iter > 0)]
panel_c = plot(iter_all, width_all;
    xlabel = "номер шага", ylabel = "величина, ч (лог. шкала)", yscale = :log10,
    title = "C. Сходимость метода", marker = :circle, color = :steelblue,
    label = "ширина отрезка (b − a)")
plot!(panel_c, iter_all, [B0_H / 2^(i - 1) for i in iter_all];
    linestyle = :dash, color = :black, label = "теория (b − a)/2ⁿ")
plot!(panel_c, iter_all, error_all;
    marker = :square, color = :red, label = "фактическая ошибка |m − t*|")

plot(panel_c, [0, last_iter], [XTOL_H, XTOL_H]; color = :green, linestyle = :dot,
    linewidth = 2, label = "допуск по аргументу")

# Панель D: крупный план окрестности корня — последние шаги и финиш.
# По оси абсцисс откладываем не само время, а отклонение от корня в 10⁻⁶ ч:
# в масштабе последних шагов миллионные доли часа читаются лучше, чем 15.350567 ч.
const ZOOM_SCALE = 1e-6
x_left = (tail_steps[1].a - T_EXACT_H) / ZOOM_SCALE
x_right = (tail_steps[1].b - T_EXACT_H) / ZOOM_SCALE
half_range = 1.1 * max(abs(x_left), abs(x_right))       # симметричное окно вокруг корня
x_zoom = (-half_range, half_range)
t_zoom = range(x_zoom[1], x_zoom[2]; length = 200)
t_zoom_abs = T_EXACT_H .+ t_zoom .* ZOOM_SCALE          # те же точки в абсолютном времени
ticks_zoom = range(x_zoom[1], x_zoom[2]; length = 5)
panel_d = plot(t_zoom, residual.(t_zoom_abs);
    label = "f(t) = C(t) − C_МТК",
    xlabel = "отклонение от корня (t − t*)·10⁶, ч", ylabel = "f(t), мг/л",
    title = "D. Финиш: последние $(length(tail_steps)) шагов",
    linewidth = 2, color = :navy, legend = :topright, xlims = x_zoom,
    xticks = (collect(ticks_zoom), [string(round(x, digits = 2)) for x in ticks_zoom]))
hline!(panel_d, [0.0]; color = :black, linestyle = :dash, linewidth = 1, label = "нулевой уровень")
vline!(panel_d, [0.0]; color = :green, linestyle = :dot, linewidth = 2, label = "точный корень t*")
scatter!(panel_d, [(st.m - T_EXACT_H) / ZOOM_SCALE for st in tail_steps], [st.fm for st in tail_steps];
    color = :red, markersize = 6, markerstrokewidth = 0, label = "середины последних шагов")

plot(panel_d, [x_zoom[1], x_zoom[2]], [0.0, 0.0]; color = :black, linestyle = :dash, linewidth = 1, label = "" )

figure = plot(panel_a, panel_b, panel_c, panel_d;
    layout = (2, 2), size = (1200, 820), margin = 6Plots.mm,
    plot_title = "Метод бисекции: f(t) = C0·exp(−k·t) − C_МТК,  t* = " *
                 string(round(T_EXACT_H, digits = 4)) * " ч")

svg_path = joinpath(DIR_FIGURES_SVG, "bisection_steps.svg")
png_path = joinpath(DIR_FIGURES_PNG, "bisection_steps.png")
savefig(figure, svg_path)
savefig(figure, png_path)

plot(figure)  # показать рисунок в интерактивной сессии Julia

println("Рисунок SVG: ", svg_path)
println("Рисунок PNG: ", png_path)
