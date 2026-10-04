"""
newton_demo.jl — пошаговая демонстрация метода Ньютона (касательных).

Скрипт решает то же фармакокинетическое уравнение, что и bisection_demo.jl,

    f(t)  = C0 · exp(−k·t) − C_МТК = 0,
    f′(t) = −k · C0 · exp(−k·t),

методом Ньютона и показывает работу метода:

  * таблицу шагов на экране (старт, первые четыре шага, финиш):
    текущая точка xₙ, значения f(xₙ) и f′(xₙ), следующая точка xₙ₊₁ и шаг Δx;
  * полный журнал всех шагов в results/tables/newton_steps.csv;
  * рисунок из четырёх панелей в figures/svg и figures/png:
      A — график функции и касательные, которыми пользуется метод;
      B — «лестница» шагов: откуда и куда переходит приближение;
      C — сходимость по аргументу и проверка квадратичного закона;
      D — крупный план финиша: последние шаги в окрестности корня.

Запуск из корня репозитория:

    julia --project=. chapters/02_prostye_modeli_osnovy_chislennykh_metodov/julia/newton_demo.jl
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

const X0_H = 5.0            # начальное приближение, ч
const XTOL_H = 1e-6         # допуск по шагу |Δx|, ч
const MAX_ITER = 50         # страховка от зацикливания

const N_FIRST_SHOWN = 4     # сколько первых шагов показываем отдельно

"Концентрация препарата в момент времени t (ч), мг/л."
concentration(t) = C0_MG_L * exp(-K_ELIM_1H * t)

"Невязка задачи: отклонение концентрации от терапевтического порога, мг/л."
residual(t) = concentration(t) - MTC_MG_L

"Производная невязки df/dt = −k·C(t), мг/(л·ч)."
residual_derivative(t) = -K_ELIM_1H * concentration(t)

"Точное решение уравнения f(t) = 0, ч (нужно для контроля метода)."
const T_EXACT_H = log(C0_MG_L / MTC_MG_L) / K_ELIM_1H

# --------------------------------------------------------------------------
# 2. Метод Ньютона с журналом шагов
# --------------------------------------------------------------------------

"""
Один шаг метода: точка x, значения f(x) и f′(x), следующая точка x_next и шаг
delta = x_next − x.

Касательная в точке (x, f(x)) пересекает ось абсцисс именно в x_next, поэтому
запись содержит всё необходимое и для таблицы, и для геометрической картинки.
"""
struct NewtonStep
    iter::Int
    x::Float64
    fx::Float64
    dfx::Float64
    x_next::Float64
    delta::Float64
end

"""
    newton_logged(f, df, x0; xtol, max_iter) -> (root, steps)

Метод Ньютона для уравнения f(x) = 0 при известной производной df.

Остановка — по величине шага: |Δx| < xtol. Возвращает найденный корень и
вектор записей NewtonStep по одной на каждую итерацию (первая запись —
начальное приближение).
"""
function newton_logged(f, df, x0::Float64; xtol::Float64 = 1e-6, max_iter::Int = 50)
    steps = NewtonStep[]
    x = x0

    for iter in 0:max_iter
        fx, dfx = f(x), df(x)
        # При почти горизонтальной касательной шаг не определён — сообщаем об этом.
        abs(dfx) < eps(Float64) && error("Производная близка к нулю: шаг метода Ньютона не определён.")

        x_next = x - fx / dfx        # точка пересечения касательной с осью абсцисс
        delta = x_next - x
        push!(steps, NewtonStep(iter, x, fx, dfx, x_next, delta))

        abs(delta) < xtol && return x_next, steps   # шаг стал меньше допуска
        x = x_next
    end

    return x, steps
end

# --------------------------------------------------------------------------
# 3. Вывод шагов на экран
# --------------------------------------------------------------------------

"Число для таблицы: маленькие величины печатаем в экспоненциальной форме."
function fmt_value(x::Float64, digits::Int = 8)
    (x != 0.0) && (abs(x) < 1e-4) && return string(round(x, sigdigits = 3))
    return string(round(x, digits = digits))
end

"Напечатать выбранные шаги в виде таблицы с подписью «старт» и «финиш»."
function print_steps(steps::Vector{NewtonStep}, selected::Vector{Int}, last_iter::Int)
    header = ("шаг", "xₙ, ч", "f(xₙ), мг/л", "f′(xₙ), мг/(л·ч)", "xₙ₊₁, ч", "Δx, ч")
    widths = (8, 15, 15, 17, 15, 13)
    println(join(lpad.(header, widths), " "))
    println("-"^86)
    for st in steps
        st.iter in selected || continue
        label = st.iter == 0 ? "старт" : (st.iter == last_iter ? "финиш" : string(st.iter))
        row = (label, fmt_value(st.x), fmt_value(st.fx), fmt_value(st.dfx),
               fmt_value(st.x_next), fmt_value(st.delta))
        println(join(lpad.(row, widths), " "))
    end
end

# --------------------------------------------------------------------------
# 4. Запуск метода
# --------------------------------------------------------------------------

t_root, steps = newton_logged(residual, residual_derivative, X0_H; xtol = XTOL_H, max_iter = MAX_ITER)
last_iter = steps[end].iter

# Показываем старт, первые N_FIRST_SHOWN шагов и финиш.
selected = vcat(0, collect(1:N_FIRST_SHOWN), last_iter)

println("\nМетод Ньютона: f(t) = C(t) − C_МТК, старт x₀ = $(X0_H) ч, допуск по шагу $(XTOL_H) ч")
print_steps(steps, selected, last_iter)

println("\nНайдено:  t = ", round(t_root, digits = 9), " ч за ", last_iter, " итераций")
println("Точно:    t = ", round(T_EXACT_H, digits = 9), " ч (формула ln(C0/C_МТК)/k)")
println("Ошибка по аргументу: ", abs(t_root - T_EXACT_H), " ч")
println("Проверка: C(t) = ", round(concentration(t_root), digits = 9),
        " мг/л вместо ", MTC_MG_L, " мг/л")

# --------------------------------------------------------------------------
# 5. Полный журнал шагов в CSV
# --------------------------------------------------------------------------

csv_path = joinpath(DIR_RESULTS_TABLES, "newton_steps.csv")
CSV.write(csv_path, (
    step = [st.iter for st in steps],
    x_h = [st.x for st in steps],
    f_x_mg_l = [st.fx for st in steps],
    df_x_mg_l_h = [st.dfx for st in steps],
    x_next_h = [st.x_next for st in steps],
    delta_h = [st.delta for st in steps],
))
println("\nЖурнал шагов: ", csv_path)

# --------------------------------------------------------------------------
# 6. Рисунок: четыре панели
# --------------------------------------------------------------------------

first_steps = [st for st in steps if 1 <= st.iter <= N_FIRST_SHOWN]        # шаги 1–4
tangent_steps = vcat(steps[1:1], first_steps)                              # старт + шаги 1–4
ladder = vcat(steps[1:1], first_steps, steps[end:end])                     # старт, 1–4, финиш
tail_steps = [st for st in steps if st.iter > last_iter - 3]               # последние три шага

# Панель A: функция и касательные, которыми «шагает» метод.
t_curve = range(3.0, 24.0; length = 400)
panel_a = plot(t_curve, residual.(t_curve);
    label = "f(t) = C(t) − C_МТК",
    xlabel = "время t, ч", ylabel = "f(t), мг/л",
    title = "A. Касательные метода Ньютона",
    linewidth = 2, color = :navy, legend = :topright, xlims = (3.0, 24.0))
hline!(panel_a, [0.0]; color = :black, linestyle = :dash, linewidth = 1, label = "нулевой уровень")
vline!(panel_a, [T_EXACT_H]; color = :green, linestyle = :dot, linewidth = 2, label = "точный корень t*")
for (k, st) in enumerate(tangent_steps)
    # Касательная в точке (x, f(x)) и её пересечение с осью абсцисс в x_next.
    plot!(panel_a, [st.x, st.x_next], [st.fx, 0.0];
        color = :gray, linestyle = :dash, linewidth = 1,
        label = k == 1 ? "касательные" : "")
    scatter!(panel_a, [st.x], [st.fx]; color = :red, markersize = 6,
        markerstrokewidth = 0, label = k == 1 ? "точки xₙ на кривой" : "")
    scatter!(panel_a, [st.x_next], [0.0]; color = :orange, markershape = :utriangle,
        markersize = 6, label = k == 1 ? "пересечения с осью xₙ₊₁" : "")
end
annotate!(panel_a, X0_H + 0.6, residual(X0_H) + 1.2, text("x₀ — старт", 9, :red))

# Панель B: «лестница» шагов — из какой точки в какую переводит метод.
ladder_y = collect(0:-1:-(length(ladder) - 1))
ladder_labels = [st.iter == 0 ? "старт" : (st.iter == last_iter ? "финиш" : "шаг $(st.iter)")
                 for st in ladder]
panel_b = plot(; xlabel = "время t, ч", ylabel = "", yticks = (ladder_y, ladder_labels),
    title = "B. Шаги метода: xₙ → xₙ₊₁", legend = :bottomleft,
    ylims = (minimum(ladder_y) - 0.7, maximum(ladder_y) + 0.7), xlims = (4.0, 22.0))
for (k, st) in enumerate(ladder)
    y = ladder_y[k]
    plot!(panel_b, [st.x, st.x_next], [y, y];
        color = :steelblue, linewidth = 7, label = k == 1 ? "переход xₙ → xₙ₊₁" : "")
    scatter!(panel_b, [st.x], [y]; color = :red, markersize = 4,
        label = k == 1 ? "текущая точка xₙ" : "")
    annotate!(panel_b, 19.2, y, text("Δx = " * fmt_value(st.delta, 4), 8, :black))
end
vline!(panel_b, [T_EXACT_H]; color = :green, linestyle = :dot, linewidth = 2, label = "точный корень t*")

# Панель C: сходимость и проверка квадратичного закона eₙ₊₁ ≈ C·eₙ².
iter_all = [st.iter for st in steps]
err_all = [abs(st.x - T_EXACT_H) for st in steps]            # ошибка в текущей точке xₙ
delta_all = [abs(st.delta) for st in steps]                  # величина шага |Δx|

const QUADRATIC_FROM = 2    # шаг, с которого проверяем квадратичный закон
# В записи с индексом i хранится ошибка eᵢ₋₁ = |xᵢ₋₁ − t*|, поэтому
# C = e₃/e₂² берётся по записям 4 и 3.
const C_MODEL = err_all[QUADRATIC_FROM + 2] / err_all[QUADRATIC_FROM + 1]^2
model_curve = fill(NaN, length(steps))
model_curve[QUADRATIC_FROM + 2] = err_all[QUADRATIC_FROM + 2]
for i in (QUADRATIC_FROM + 2):(length(steps) - 1)
    model_curve[i + 1] = C_MODEL * model_curve[i]^2
end

# Шаг метода меняется от единиц часов до 10⁻⁷ ч, а найденный корень совпадает
# с точным до 10⁻¹⁵ ч — отметки задаём явно через каждые три декады.
const YTICKS_C = 10.0 .^ collect(1:-3:-14)
const ERR_ROOT_H = abs(t_root - T_EXACT_H)   # ошибка точки, которую вернул метод

panel_c = plot(iter_all, max.(err_all, eps());
    xlabel = "номер шага", ylabel = "величина, ч (лог. шкала)", yscale = :log10,
    title = "C. Сходимость метода", marker = :circle, color = :red,
    label = "ошибка |xₙ − t*|", yticks = YTICKS_C, ylims = (1e-16, 3e1),
    legend = :bottomleft)
plot!(panel_c, iter_all, max.(delta_all, eps());
    marker = :diamond, color = :orange, label = "шаг |Δx|")
plot!(panel_c, iter_all, model_curve;
    linestyle = :dash, color = :black, linewidth = 2,
    label = "квадратичный закон C·eₙ² (C по шагу $(QUADRATIC_FROM))")
scatter!(panel_c, [last_iter], [max(ERR_ROOT_H, eps())];
    marker = :star5, color = :green, markersize = 9, markerstrokewidth = 0,
    label = "ошибка найденного корня")
annotate!(panel_c, 2.1, 6,
    text("остановка по допуску |Δx| < $(XTOL_H) ч:\n" *
         "последний шаг " * fmt_value(abs(steps[end].delta), 3) * " ч,\n" *
         "а точка xₙ₊₁ совпала с корнем до $(fmt_value(ERR_ROOT_H, 3)) ч", 8, :green))


# Панель D: крупный план финиша — последние три шага в окрестности корня.
# По оси абсцисс откладываем отклонение от корня в 10⁻³ ч: в масштабе последних
# шагов тысячные доли часа читаются лучше, чем 15.350567 ч.
const ZOOM_SCALE = 1e-3
dev_x(st) = (st.x - T_EXACT_H) / ZOOM_SCALE
half_range = 1.1 * abs(dev_x(tail_steps[1]))        # симметричное окно вокруг корня
x_zoom = (-half_range, half_range)
t_zoom = range(x_zoom[1], x_zoom[2]; length = 300)
t_zoom_abs = T_EXACT_H .+ t_zoom .* ZOOM_SCALE      # те же точки в абсолютном времени
ticks_zoom = range(x_zoom[1], x_zoom[2]; length = 4)
panel_d = plot(t_zoom, residual.(t_zoom_abs);
    label = "f(t) = C(t) − C_МТК",
    xlabel = "отклонение от корня (t − t*)·10³, ч", ylabel = "f(t), мг/л",
    title = "D. Финиш: последние 3 шага",
    linewidth = 2, color = :navy, legend = :topright, xlims = x_zoom,
    xticks = (collect(ticks_zoom), [string(round(x, digits = 1)) for x in ticks_zoom]))
hline!(panel_d, [0.0]; color = :black, linestyle = :dash, linewidth = 1, label = "нулевой уровень")
vline!(panel_d, [0.0]; color = :green, linestyle = :dot, linewidth = 2, label = "точный корень t*")
for st in tail_steps
    plot!(panel_d, [dev_x(st), (st.x_next - T_EXACT_H) / ZOOM_SCALE], [st.fx, 0.0];
        color = :gray, linestyle = :dash, linewidth = 1, label = "")
    scatter!(panel_d, [dev_x(st)], [st.fx]; color = :red, markersize = 6,
        markerstrokewidth = 0, label = "")
end
scatter!(panel_d, [dev_x(st) for st in tail_steps], [st.fx for st in tail_steps];
    color = :red, markersize = 6, markerstrokewidth = 0, label = "точки xₙ последних шагов")
annotate!(panel_d, -0.6 * half_range, -0.03,
    text("xₙ последних шагов\nпрактически совпадают с t*", 8, :red))

figure = plot(panel_a, panel_b, panel_c, panel_d;
    layout = (2, 2), size = (1200, 820), margin = 6Plots.mm,
    plot_title = "Метод Ньютона: f(t) = C0·exp(−k·t) − C_МТК,  старт " * string(X0_H) *
                 " ч,  t* = " * string(round(T_EXACT_H, digits = 4)) * " ч")

svg_path = joinpath(DIR_FIGURES_SVG, "newton_steps.svg")
png_path = joinpath(DIR_FIGURES_PNG, "newton_steps.png")
savefig(figure, svg_path)
savefig(figure, png_path)

println("Рисунок SVG: ", svg_path)
println("Рисунок PNG: ", png_path)
