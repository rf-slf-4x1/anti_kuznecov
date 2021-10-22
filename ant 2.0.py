# импорт необходимых модулей
import sympy as sym
import matplotlib.pyplot as plt

# получаем необходимые данные для начала решения
x1 = float(input('Введите координату Х начальной точки: '))
y1 = float(input('Введите координату Y начальной точки: '))
x2 = float(input('Введите координату Х конечной точки: '))
y2 = float(input('Введите координату Y конечной точки: '))
xd = float(input('Введите координату Х центра дерева: '))
yd = float(input('Введите координату Y центра дерева: '))
r = float(input('Введите радиус ствола дерева: '))

# Задаем х и у как координаты - переменные0 для символьного решения
x = sym.Symbol('x')
y = sym.Symbol('y')

# Составляем уравнение окружности - ствол дерева
uravn_circle = ((x-xd)**2 + (y-yd)**2 - r**2)

# Составляем уравнение прямой - пути
uravn_line = sym.simplify((y1-y2)*x + (x2-x1)*y + (x1*y2 - x2*y1))

# Находим количество пересечений этих уравнений
points = sym.solvers.solve([uravn_line, uravn_circle], (x, y))
number_of_elements = len(points)

if x1 == x2 and y1 == y2:
    # проверяем, если координаты не изменились
    print('Муравей не сдвинулся с места')
else:
    # рассматриваем количество решений
    if number_of_elements == 1 or number_of_elements == 0:
        # Если муравей не упирался в ствол или прошел по касательной
        s1 = sym.sqrt((x2-x1)**2+(y2-y1)**2)        # расстояние строго между двумя точками
        print(f'На пути муравья нет дерева, его путь будет равен {s1}')

    elif number_of_elements == 2:        # если муравей уперся в ствол
        # проверяем на наличие ошибки
        str_points = str(points)
        if 'I' in str_points:
            print('Нет решений в декартовой системе координат')
        else:
            if (x1-xd)**2 + (y1-yd)**2 < r**2 or (x2-xd)**2 + (y2-yd)**2 < r**2:
                print('Ошибка входных данных! Координаты начала или конца пути лежат внутри дерева')
            else:
                m1 = (sym.sqrt((xd-x1)**2 + (yd-y1)**2 - r**2))     # длина касательной от начальной точки
                m2 = (sym.sqrt((x2-xd)**2 + (y2-yd)**2 - r**2))     # длина касательной от конечной точки
                # рассчитываем длину дуги между касательными
                k = ((y2-y1)/(x2-x1))
                temp_1 = (sym.sqrt((x-xd)**2 + (y-yd)**2 - r**2))
                temp_2 = (y-y1) - k * (x-x1)
                # точки пересечения хорды с окружностью находим через систему уравнений
                points_horda = sym.solve([temp_1, temp_2], (x, y))
                horda_x1 = points_horda [0][0]
                horda_y1 = points_horda [0][1]
                horda_x2 = points_horda [1][0]
                horda_y2 = points_horda [1][1]
                
                # # длина пути - две касательные плюс кусок дуги
                # print(f'На пути муравья есть дерево, путь будет равен {m1 + m2 + l}')
                # print(m1, m2, alpha, l, horda, points_horda)
                p1 = (x1, y1)       # координаты начала пути
                p2 = (x2, y2)       # координаты конца пути
                pd = (xd, yd)       # координаты центра дерева

                #Рисую график
                fig, ax = plt.subplots() 					# тело графика
                plt.title ("График для задачи")	    # название графика
                plt.xlabel("Ось X", fontsize=10, color='blue')		# ось абсцисс (x)
                plt.ylabel("Ось Y", fontsize=10, color='red') 		# ось ординат (y)
                circle = plt.Circle((xd, yd), r, fill = False)
                plt.plot([p1[0], p2[0]], [p1[1], p2[1]])
                plt.scatter(horda_x1, horda_y1, s=12, c='red', marker="o", alpha = 1)
                plt.scatter(horda_x2, horda_y2, s=12, c='red', marker="o", alpha = 1)
                plt.scatter(x1, y1, s=40, c='purple', marker="o", alpha = 1)
                plt.scatter(x2, y2, s=40, c='purple', marker="o", alpha = 1)
                ax.add_artist(circle)

                c = r

                x_isk_1_var_1 = ((1/2)*((yd-y1)*sym.sqrt(-(-xd**2+2*x1*xd-x1**2+(-c+m1-yd+y1)*(-c+m1+yd-y1))*(-xd**2+2*x1*xd-x1**2+(c+m1-yd+y1)*(c+m1+yd-y1))*(xd-x1)**2)+(xd**3-xd**2*x1+(y1**2-2*yd*y1-c**2+yd**2+m1**2-x1**2)*xd-x1*(m1**2-c**2-x1**2-y1**2+2*yd*y1-yd**2))*(xd-x1))/((xd-x1)*(xd**2-2*x1*xd+x1**2+(yd-y1)**2)))

                y_isk_1_var_1 = (-sym.sqrt(-(-xd**2+2*x1*xd-x1**2+(-c+m1-yd+y1)*(-c+m1+yd-y1))*(-xd**2+2*x1*xd-x1**2+(c+m1-yd+y1)*(c+m1+yd-y1))*(xd-x1)**2)+yd**3-yd**2*y1+(m1**2+xd**2-c**2+x1**2-2*x1*xd-y1**2)*yd+y1**3+(x1**2-2*x1*xd+c**2-m1**2+xd**2)*y1)/(2*yd**2-4*yd*y1+2*y1**2+2*(xd-x1)**2)

                x_isk_1_var_2 = (1/2)*((-yd+y1)*sym.sqrt(-(-xd**2+2*x1*xd-x1**2+(-c+m1-yd+y1)*(-c+m1+yd-y1))*(xd-x1)**2*(-xd**2+2*x1*xd-x1**2+(c+m1-yd+y1)*(c+m1+yd-y1)))+(xd-x1)*(xd**3-xd**2*x1+(yd**2-2*yd*y1+y1**2+m1**2-c**2-x1**2)*xd-x1*(-c**2-x1**2+m1**2-yd**2+2*yd*y1-y1**2)))/((xd**2-2*x1*xd+x1**2+(yd-y1)**2)*(xd-x1))

                y_isk_1_var_2 = (sym.sqrt(-(xd-x1)**2*(-xd**2+2*x1*xd-x1**2+(c+m1+yd-y1)*(c+m1-yd+y1))*(-xd**2+2*x1*xd-x1**2+(-c+m1+yd-y1)*(-c+m1-yd+y1)))+yd**3-yd**2*y1+(m1**2+xd**2-c**2+x1**2-2*x1*xd-y1**2)*yd+y1**3+(x1**2-2*x1*xd+c**2-m1**2+xd**2)*y1)/(2*yd**2-4*yd*y1+2*y1**2+2*(xd-x1)**2)



                x_isk_2_var_1 = (1/2)*((yd-y2)*sym.sqrt(-(-xd**2+2*x2*xd-x2**2+(-c+m2-yd+y2)*(-c+m2+yd-y2))*(-xd**2+2*x2*xd-x2**2+(c+m2-yd+y2)*(c+m2+yd-y2))*(xd-x2)**2)+(xd**3-xd**2*x2+(y2**2-2*yd*y2-c**2+yd**2+m2**2-x2**2)*xd-x2*(m2**2-c**2-x2**2-y2**2+2*yd*y2-yd**2))*(xd-x2))/((xd-x2)*(xd**2-2*x2*xd+x2**2+(yd-y2)**2))

                y_isk_2_var_1 = (-sym.sqrt(-(-xd**2+2*x2*xd-x2**2+(-c+m2-yd+y2)*(-c+m2+yd-y2))*(-xd**2+2*x2*xd-x2**2+(c+m2-yd+y2)*(c+m2+yd-y2))*(xd-x2)**2)+yd**3-yd**2*y2+(m2**2+xd**2-c**2+x2**2-2*x2*xd-y2**2)*yd+y2**3+(x2**2-2*x2*xd+c**2-m2**2+xd**2)*y2)/(2*yd**2-4*yd*y2+2*y2**2+2*(xd-x2)**2)

                x_isk_2_var_2 = (1/2)*((-yd+y2)*sym.sqrt(-(-xd**2+2*x2*xd-x2**2+(-c+m2-yd+y2)*(-c+m2+yd-y2))*(xd-x2)**2*(-xd**2+2*x2*xd-x2**2+(c+m2-yd+y2)*(c+m2+yd-y2)))+(xd-x2)*(xd**3-xd**2*x2+(yd**2-2*yd*y2+y2**2+m2**2-c**2-x2**2)*xd-x2*(-c**2-x2**2+m2**2-yd**2+2*yd*y2-y2**2)))/((xd**2-2*x2*xd+x2**2+(yd-y2)**2)*(xd-x2))

                y_isk_2_var_2 = (sym.sqrt(-(xd-x2)**2*(-xd**2+2*x2*xd-x2**2+(c+m2+yd-y2)*(c+m2-yd+y2))*(-xd**2+2*x2*xd-x2**2+(-c+m2+yd-y2)*(-c+m2-yd+y2)))+yd**3-yd**2*y2+(m2**2+xd**2-c**2+x2**2-2*x2*xd-y2**2)*yd+y2**3+(x2**2-2*x2*xd+c**2-m2**2+xd**2)*y2)/(2*yd**2-4*yd*y2+2*y2**2+2*(xd-x2)**2)

                cosat_1 = sym.sqrt((x_isk_1_var_1 - x1)**2 + (y_isk_1_var_1 - y1)**2)
                cosat_2 = sym.sqrt((x_isk_2_var_2 - x1)**2 + (y_isk_1_var_2 - y1)**2)
                cosat_3 = sym.sqrt((x_isk_2_var_1 - x2)**2 + (y_isk_2_var_1 - y2)**2)
                cosat_4 = sym.sqrt((x_isk_2_var_2 - x2)**2 + (y_isk_2_var_2 - y2)**2)


                if cosat_1 + cosat_3 > cosat_2 + cosat_4:

                    plt.scatter(x_isk_1_var_1, y_isk_1_var_1, s=25, c='blue', marker="x", alpha = 1)
                    plt.scatter(x_isk_2_var_1, y_isk_2_var_1, s=25, c='blue', marker="x", alpha = 1)
                    plt.plot([x_isk_1_var_1, x1], [y_isk_1_var_1, y1], c='red')
                    plt.plot([x_isk_2_var_1, x2], [y_isk_2_var_1, y2], c='red')
                    
                    horda = sym.sqrt((x_isk_2_var_1-x_isk_1_var_1)**2+(y_isk_2_var_1-y_isk_1_var_1)**2)     #находим длину хорды
                    alpha = (2 * (sym.asin((horda)/(2*r))))                             # находим центральный угол
                    l = r * alpha
                
                    # длина пути - две касательные плюс кусок дуги
                    print(f'На пути муравья есть дерево, путь будет равен {m1 + m2 + l}')

                else:

                    plt.scatter(x_isk_1_var_2, y_isk_1_var_2, s=25, c='blue', marker="x", alpha = 1)
                    plt.scatter(x_isk_2_var_2, y_isk_2_var_2, s=25, c='blue', marker="x", alpha = 1)
                    plt.plot([x_isk_1_var_2, x1], [y_isk_1_var_2, y1], c='red')
                    plt.plot([x_isk_2_var_2, x2], [y_isk_2_var_2, y2], c='red')
                    
                    horda = sym.sqrt((x_isk_2_var_2-x_isk_1_var_2)**2+(y_isk_2_var_2-y_isk_1_var_2)**2)     #находим длину хорды
                    alpha = (2 * (sym.asin((horda)/(2*r))))                             # находим центральный угол
                    l = r * alpha
                
                    # длина пути - две касательные плюс кусок дуги
                    print(f'На пути муравья есть дерево, путь будет равен {m1 + m2 + l}')


                ax.grid(True)
                d = 2 * r
                ax.set_xlim(-2 * d, 2 * d)
                ax.set_ylim(-2 * d, 2 * d)
                plt.gca().set_aspect("equal")
                plt.show()
