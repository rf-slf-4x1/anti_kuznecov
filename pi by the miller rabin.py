# Чернышев Дмитрий 421 группа РФФ
import matplotlib.pyplot as plt
from random import random
import timeit
st1 = timeit.default_timer()
inside = 0      # задание переменной
n = 10**4       # количество точек

x_inside = []       # создаем пустой список кооринат точек внутри круга по х
y_inside = []       # создаем пустой список кооринат точек внутри круга по у
x_outside = []      # создаем пустой список кооринат точек извне круга по х
y_outside = []      # создаем пустой список кооринат точек извне круга по у

for temp in range(n):       # перебираем все точки
    x = random()            # задаем случайные координаты х
    y = random()            # задаем случайные координаты у
    if x**2+y**2 <= 1:      # "рисуем" окружность и проверяем местоположение точки
        inside += 1         # добавляем число в переменную если точка внутри
        x_inside.append(x)  # вставляем в конец списка координату х
        y_inside.append(y)  # вставляем в конец списка координату у
    else:
        x_outside.append(x) # вставляем в конец списка координату х
        y_outside.append(y) # вставляем в конец списка координату у

# находим число pi методом Монте-Карло
pi = 4*inside/n
print('При количестве точек ' + str(n) + ' помощью метода Монте-Карло получили значение pi равное: ' + str(pi))

plt.figure() 					# тело графика
plt.title ("Расположение точек")	    # название графика
plt.xlabel("Ось X", fontsize=10, color='blue')		# ось абсцисс (x)
plt.ylabel("Ось Y", fontsize=10, color='red') 		# ось ординат (y)
plt.scatter(x_inside, y_inside, s=7, c='red', marker="o", alpha = 1, label='Точки внутри круга')
plt.scatter(x_outside, y_outside, s=7, c='blue', marker="o", alpha = 1, label='Точки извне круга')
plt.legend()   			# Отобразить легенду - label
st2 = timeit.default_timer()
plt.show()

print("RUN TIME : {0}".format(st2-st1))
