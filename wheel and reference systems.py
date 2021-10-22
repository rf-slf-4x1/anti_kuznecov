# Мищенко Евгения 421 группа

from math import pi

# функция перевода числа number в систему счисления с основанием n
def changing_the_number_system(number, n):
    result = ''
    while number > 0:
        result = str(number % n) + result
        number = number // n
    return int(result)

# функция подсчета пройденного расстояния
S = lambda x: int(2*pi*x*50000/100/1000)


#количество проверяемых оснований счислений
count = 100000

Rx = 101
N = 50000
Lx = 313

for n in range(4, count):
    R = changing_the_number_system(Rx, n)
    # print(R)
    L = changing_the_number_system(Lx, n) * 1e5
    if R*2*pi*N == L:
        print(n)

# print(f'Основание системы счисления: {R}')
# r = R*R+1
# print(f'Радиус: {r} см')
# dist10 = S(r)
# print(f'Перемещение в десятичной системе счисления: {dist10} км')
# print(f"Рассчитанные значения проверим, посчитав перемещение в системе счисления с основанием R = {7}")
# check = 313
# distR = ''
# while dist10 > 0:
#     distR = str(dist10 % R) + distR
#     dist10 = dist10 // R
# print(f'Перемещение в системе счисления с основанием {R}: {distR} км')
# if int(distR) == check: print("Проверка пройдена, задача решена верно")
# else: print("Проверка не пройдена, задача решена с ошибкой")
