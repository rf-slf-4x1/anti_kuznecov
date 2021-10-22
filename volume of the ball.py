import numpy as np
import math
import matplotlib.pyplot as plt

def shar(n, N):            # N точек, на каждую n проэкций по осям
    points = np.random.rand(N,n)    # создаем рандомные точки в первой четверти пространства
    radius = np.sqrt((points**2).sum(1))       # считаем расстояние для всех точек
    # смотрим количество точек которые лежат внутри сферы
    ninside = (radius < 1).sum()
    # смотрим отношение точек внутри ко всем и домнажаем на количество "четвертей" в пространстве
    return ((math.log(2) * ninside * 2**n)/N)

vs = np.zeros(20)           # пустой масив для объемов в разных размерностях
for n in np.arange(1,20):   # считаем для размерностей от 1 до 25
    v = shar(n, 1000000)
    print('Объем шара радиуса ' + str(n) +  ' = ' + str(v))
    vs[n] = v

# # рисуем график
plt.figure()
plt.grid(True)
plt.scatter(np.arange(20), vs, c='blue', s=15)
plt.xlabel('Размерность')
plt.ylabel('Объем')
plt.show()
