import math
import sympy as sp
from sympy import cos, Eq, solve

# Определение функции
def f(x):
    return 8 * math.cos(x) - x - 6

# Проверка существует ли корень на задданом отрезке для данной ункции
x1, x2 = 0, 1
if f(x1) * f(x2) < 0:
    print('Корень существует на заданом отрезке [0;1]')
else: print('Корень не существует на заданом отрезке [0;1]')

# Находим значение внутри arccos при выражении выражения через cosx
x = sp.Symbol('x')
eq = Eq(8 * cos(x) - x - 6, 0)
cos_solution = solve(eq, cos(x))  
print('Знаечние функции внутри arccos:', cos_solution)

# Определение функции
def phi(x):
    return math.acos((x / 8) + (3 / 4)) 

# Нахождение производной функции
x_sym = sp.Symbol('x')
phi_expr = sp.acos((x_sym / 8) + (3 / 4))
phi_derivative = sp.diff(phi_expr, x_sym)
print('функция:', phi_expr)
print('Производная функции:', phi_derivative)

# Нахождения максимального значения производной ункции на заданом отрезке и проверяем, чтобы было меньше 1
phi_derivative_x1 = phi(x1) 
phi_derivative_x2 = phi(x2) 
max_phi_derivative = max(abs(phi_derivative_x1), abs(phi_derivative_x2))

if max_phi_derivative < 1:
    print('Значение L соблюдает условиe, будучи меньше одного = ', max_phi_derivative)
else: print('Значение L не соблюдает условиe, будучи больше одного = ', max_phi_derivative)

#Берем среднее значение отрезка за начальное число и начинаем счиать корень, пока не получим с ошибкой менее 0.001
x0 = 0.5
x_vals = [x0]
eps = 0.001
iter_count = 0

while True:
    x1 = phi(x0)
    x_vals.append(x1)
    iter_count += 1
    if abs(x1 - x0) < eps:
        break
    x0 = x1

root = x1

print(f'Корень уравнения с ошибкой меньше 0.001 = {root}, это получился x{iter_count} по счету')
