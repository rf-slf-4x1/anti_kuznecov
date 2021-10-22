from random import randint
import sys

def galton(h, b):       # h - количество столбцов, b - количество шариков
    containers = [0] * (h + 1)      # создаем пустые столбцы в кол-ве h
    for temp in range(b):           # пока шарики не кончились:
        position = 0                # начинаем движение с начала
        for i in range(0, h):       # пока столбцы не кончились
            turn = randint(0, 1)    # выбор направления
            if turn == 1:           # меняем направление на следующий столбик
                position += 1
        containers[position] = containers[position] + 1
        # если направление не изменилось шарик падает в столбик под ним
    return containers

def print_graph(dataset):
    for kol_vo in dataset:            # перебираем по данным количествам
        for i in range(0, kol_vo):    # пока количество не превышено
            print('●', end='')        # рисуем шарик
        print(kol_vo)                 # пишем сколько шариков

# containers = galton(h=int(sys.argv[1]), b=int(sys.argv[2]))
containers = galton(7, 200)
# берем данные из CMD
print_graph(containers)
# рисуем
