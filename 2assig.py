import math
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker

# Определение функций
def f(x):
    return 8 * math.cos(x) - x - 6

def y1(x):
    return 8 * math.cos(x)

def y2(x):
    return 6 + x

# СОздание графика
x_vals = np.linspace(-15, 15, 500)
y1_vals = [y1(x) for x in x_vals]
y2_vals = [y2(x) for x in x_vals]
fig, ax = plt.subplots()
ax.plot(x_vals, y1_vals, color='green', label='y=8cosx')
ax.plot(x_vals, y2_vals, color='blue', label='y=x+6')
ax.xaxis.set_major_locator(ticker.MultipleLocator(1)) 
ax.xaxis.set_minor_locator(ticker.MultipleLocator(0.1))
plt.grid(True)
plt.xlabel('Ось х')
plt.ylabel('Ось y')
plt.title('График функций')

# Нахождение интервалов, внутри которых существует корень
intervals = []
step = 0.1
x = -15
while x < 15:
    if f(x) * f(x + step) < 0:
        intervals.append((x, x + step))
    x += step

# Уточнение корня на каждом интервале
roots = []
for interval in intervals:
    x1, x2 = interval
    eps = 0.001
    while abs(x2 - x1) > eps:
        c = (x1 + x2) / 2
        if f(x1) * f(c) <= 0:
            x2 = c
        else:
            x1 = c
    root = (x1 + x2) / 2
    roots.append(root)

y_roots = [y1(r) for r in roots]
ax.plot(roots, y_roots, 'ro', label='Корни')  

for i in range(len(intervals)):
        print(f'Интервал №{i+1} = {intervals[i]}, корень на нем с ошибкой менее 0.001 равен = {roots[i]}')
plt.show()