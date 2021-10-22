# площадь многоугольника по координатам вершин
# импортируем библитеки
import matplotlib.pyplot as plt

# получаем число вершин
N = int(input('Введите количество вершин N: '))

# создаем два массива для хранения координат вершин
x = []
y = []

# получаем координаты вершин и добавляем их в списки
for i in range(N):
    temp_x = float(input('Введите x: '))
    temp_y = float(input('Введите y: '))
    x.append(temp_x)
    y.append(temp_y)

# считаем первую часть формулы Гаусса (со знаком "+")
def reskx():
    reskx = 0
    for i in range(N):
        temp = x[i - 1] * y[i]
        reskx += temp
    return reskx

# считаем вторую часть формулы Гаусса (со знаком "-")
def resky():
    resky = 0
    for i in range(N):
        temp = x[i] * y[i - 1]
        resky += temp
    return resky

# присваиваем результат функций переменным
reskx = reskx()
resky = resky()

# считаем площадь по формуле Гаусса
resxy = abs(reskx - resky)/2
print(f"Площадь многоугольника: {resxy}")

# замыкаем фигуру для рисунка
x.append(x[0])
y.append(y[0])

# делаем рисунок
plt.plot(x, y)
plt.grid()
plt.show()