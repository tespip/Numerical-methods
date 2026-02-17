import math
import sympy as sp

# Определение функции
def f(x):
    return 8 * math.cos(x) - x - 6

# Нахождение интервалов, внутри которых существует корень
intervals = []
step = 0.1
x = -15
while x < 15:
    if f(x) * f(x + step) < 0:
        intervals.append((x, x + step))
    x += step

# Определение ункции для метода хорд
def x_n_secant_method(c, x):
    return (c * f(x) - x * f(c)) / (f(x) - f(c))

# Нахождение производной и двойной производной функции
x_sym = sp.Symbol('x')
f_expr = 8 * sp.cos(x_sym) - x_sym - 6
f_derivative_1 = sp.diff(f_expr, x_sym)
f_derivative_2 = sp.diff(f_derivative_1, x_sym)
print('функция:', f_expr)
print('Производная функции:', f_derivative_1)
print('Двойная производная функции:', f_derivative_2)

# Определение производных
def f_derivative(x):
    return -8 * math.sin(x) - 1

def f_derivative2(x):
    return -8 * math.cos(x)

# # Метод хорд
# Определение фиксированного и удаляющего значения и минимума модуля производной для вычислений
values_secant_method = []
for x1, x2 in intervals:
    m = min(abs(f_derivative(x1)), abs(f_derivative(x2)))

    f_x1_secant_method = f(x1)
    f_x2_secant_method = f(x2)
    f_derivative2_x1 = f_derivative2(x1)
    f_derivative2_x2 = f_derivative2(x2)
    if f_x1_secant_method * f_derivative2_x1 > 0:
        c, x = x1, x2
    else: c, x = x2, x1
    values_secant_method.append((c, x, m))

#Расчет корня с ошибкой менее 0.001 по методу хорд
roots_secant_method = []
iters__secant_method = []
iter_count = 0
eps = 0.001

for c, x, m in values_secant_method:
    iter_count = 0
    while True:
        x1 = x_n_secant_method(c, x)
        iter_count += 1

        if abs(f(x1)) / m < eps:
            roots_secant_method.append(x1)
            iters__secant_method.append(iter_count)
            break

        x = x1

print('\nМетод хорд:')
for i in range(len(roots_secant_method)):
        print(f'x{i+1} с ошибкой меньше 0.001 = {roots_secant_method[i]}, это получился x{iters__secant_method[i]} по счету')


# # Метод касательных
# Определение ункции для метода касательных
def x_n_tangent_method(x):
    return x - (f(x) / f_derivative(x))

# Определение фиксированного и удаляющего значения и минимума модуля производной для вычислений
values_tangent_method = []
for x1, x2 in intervals:
    m = min(abs(f_derivative(x1)), abs(f_derivative(x2)))

    f_x1_tangent_method = f(x1)
    f_x2_tangent_method = f(x2)
    f_derivative2_x1_tangent_method = f_derivative2(x1)
    f_derivative2_x2_tangent_method = f_derivative2(x2)
    if f_x1_tangent_method * f_derivative2_x1_tangent_method > 0:
        c, x = x2, x1
    else: c, x = x1, x2
    values_tangent_method.append((c, x, m))

#Расчет корня с ошибкой менее 0.001 по методу касательных
roots_tangent_method = []
iters_tangent_method = []
iter_count = 0

for c, x, m in values_tangent_method:
    iter_count = 0
    while True:
        x1 = x_n_tangent_method(x)
        iter_count += 1

        if abs(f(x1)) / m < eps:
            roots_tangent_method.append(x1)
            iters_tangent_method.append(iter_count)
            break

        x = x1
        
print('\nМетод касательных:')
for i in range(len(roots_tangent_method)):
        print(f'x{i+1} с ошибкой меньше 0.001 = {roots_tangent_method[i]}, это получился x{iters_tangent_method[i]} по счету')