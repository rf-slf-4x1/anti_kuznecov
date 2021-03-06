import matplotlib.pyplot as plt
import numpy as np

a,b,c = 5, -2, 2

x_1 = np.linspace(-5, 5, 1024)
x_for_line = np.array(x_1)
y_1 = (-c -(a*x_1)/b)
y_for_line = np.array(y_1)

# вводим координаты каждой точки в виде (x,y) - получим list of tuples
dots = [(1, 3),(2, 4),(2, 1),(0, 0),(1, -1),(-1, -1),(-3, 2),(0, 1), (4, -10), (4, -15)]

x_array = []
y_array = []

for i in dots:
    x_array.append(i[0])
    y_array.append(i[1])

xx = np.array(x_array)
yy = np.array(y_array)


# в массив pos пойдут точки, лежащие по одну сторону от прямой, а в массив neg - по другую. Критерий отбора: знак выражения a*x+b*y+c
pos=[]
neg=[]

for (x,y) in dots:
 # исключаем из рассмотрения точки, лежащие на самой прямой:
 if a*x+b*y+c == 0: continue

 if a*x+b*y+c > 0: pos.append((x,y))
 else: neg.append((x,y))

# в r будет лежать максимальный найденный на данном шаге квадрат расстояния между двумя точками. Изначально тут пусто.
r = None

# в t1, t2 будут лежать координаты точек, давших максимальное расстояние

# один цикл вложен в другой: для каждой pos-точки перебираем все neg-точки
for (x,y) in pos:
    for (x2,y2) in neg:
        # вычисляем квадрат расстояния между текущими двумя точками
        d = (x-x2)**2 + (y-y2)**2

    # идем сюда, если это не первая пара точек
    if r:
    # обновляем только когда новое расстояние > старого
        if d>r:
            t1=x,y
            t2=x2,y2
            r=d

    # идем сюда, если это самая первая пара точек
    else:
        t1=x,y
        t2=x2,y2
        r=d

# максимальное расстояние, коорд-ты 1-й точки, коорд-ты 2-й точки
print(f"Максимальное расстояние: {r**0.5}, координаты: {t1}, {t2}")

fig = plt.figure() 					# тело графика
plt.title ("Рисунок")	    # название графика
plt.xlabel("Ось X", fontsize=10, color='blue')		# ось абсцисс (x)
plt.ylabel("Ось Y", fontsize=10, color='red') 		# ось ординат (y)
plt.scatter(xx, yy, s = 25, c = 'red', marker = "o", alpha = 1)     # отображение точек
plt.grid(True)                                # включение отображения стандартой сетки
plt.plot(x_for_line, y_for_line)        # график - апрокимация (прямая)
plt.show()
