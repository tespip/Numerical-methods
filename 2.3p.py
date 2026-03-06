# Задача 2
from math import sin, cos
import sympy as sp
from sympy import cos, Eq, solve

# Определение функции
def f(x):
    return x * sin(x) - 1

# Проверка существует ли корень на задданом отрезке для данной ункции
x1, x2 = 1, 2
if f(x1) * f(x2) < 0:
    print('Корень существует на заданом отрезке [1;2]')
else: print('Корень не существует на заданом отрезке [1;2]')

# Определение функции
def phi(x):
    return 1 / sin(x)

# Нахождение производной функции
x_sym = sp.Symbol('x')
phi_expr = 1 / sp.sin(x_sym)
phi_derivative = sp.diff(phi_expr, x_sym)
print('функция:', phi_expr)
print('Производная функции:', phi_derivative)

def derivative(x):
    return - (cos(x)) / (sin(x) ** 2)

# Нахождения максимального значения производной ункции на заданом отрезке и проверяем, чтобы было меньше 1
phi_derivative_x1 = derivative(x1) 
phi_derivative_x2 = derivative(x2) 
max_phi_derivative = max(abs(phi_derivative_x1), abs(phi_derivative_x2))

if max_phi_derivative < 1:
    print('Значение L соблюдает условиe, будучи меньше одного = ', max_phi_derivative)
else: print('Значение L не соблюдает условиe, будучи больше одного = ', max_phi_derivative)

#Берем среднее значение отрезка за начальное число и начинаем счиать корень, пока не получим с ошибкой менее 0.001
x0 = 1.5
x_vals = [x0]
eps = 0.00001
iter_count = 0

while True:
    x1 = phi(x0)
    x_vals.append(x1)
    iter_count += 1
    if abs(x1 - x0) < eps:
        break
    x0 = x1

root = x1

print(f'Корень уравнения с ошибкой меньше 0.00001 = {root}, это получился x{iter_count} по счету')
