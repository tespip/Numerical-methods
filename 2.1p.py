from math import log10
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker

# Определение функций
def f(x):
    return log10(x) + 6 - (x**2)

def y1(x):
    return log10(x)

def y2(x):
    return (x**2) - 6

# СОздание графика
x_vals = np.linspace(0.1, 5, 500)
y1_vals = [y1(x) for x in x_vals]
y2_vals = [y2(x) for x in x_vals]
fig, ax = plt.subplots()
ax.plot(x_vals, y1_vals, color='green', label='y=log10(x)')
ax.plot(x_vals, y2_vals, color='blue', label='y=x*2-6')
ax.xaxis.set_major_locator(ticker.MultipleLocator(1)) 
ax.xaxis.set_minor_locator(ticker.MultipleLocator(0.1))
plt.grid(True)
plt.xlabel('Ось х')
plt.ylabel('Ось y')
plt.title('График функций')

# Нахождение интервалов, внутри которых существует корень
intervals = []
step = 0.1
x = 0.1
while x < 5:
    if f(x) * f(x + step) < 0:
        intervals.append((x, x + step))
    x += step

for i in range(len(intervals)):
        print(f'Интервал №{i+1} = {intervals[i]}')
plt.show()



# from math import sin
# import numpy as np
# import matplotlib.pyplot as plt
# import matplotlib.ticker as ticker

# # Определение функций
# def f(x):
#     return x * sin(x) - 1

# def y1(x):
#     return x * sin(x) 

# def y2(x):
#     return 1

# # СОздание графика
# x_vals = np.linspace(-10, 10, 500)
# y1_vals = [y1(x) for x in x_vals]
# y2_vals = [y2(x) for x in x_vals]
# fig, ax = plt.subplots()
# ax.plot(x_vals, y1_vals, color='green', label='y=xsinx')
# ax.plot(x_vals, y2_vals, color='blue', label='y=1)
# ax.xaxis.set_major_locator(ticker.MultipleLocator(1)) 
# ax.xaxis.set_minor_locator(ticker.MultipleLocator(0.1))
# plt.grid(True)
# plt.xlabel('Ось х')
# plt.ylabel('Ось y')
# plt.title('График функций')

# # Нахождение интервалов, внутри которых существует корень
# intervals = []
# step = 0.1
# x = -5
# while x < 5:
#     if f(x) * f(x + step) < 0:
#         intervals.append((x, x + step))
#     x += step

# for i in range(len(intervals)):
#         print(f'Интервал №{i+1} = {intervals[i]}')
# plt.show()