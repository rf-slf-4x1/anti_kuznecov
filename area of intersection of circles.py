import math
import matplotlib.pyplot as plt
x1 = 0
y1 = 0
r1 = 5
x2 = 5
y2 = 5
r2 = 7

d = math.sqrt((x2-x1)**2 + (y2-y1)**2) 

def search_s(d, r1, r2):
    try:
        f1 = 2 * math.acos((r1**2-r2**2+d**2)/(2*r1*d))
        f2 = 2 * math.acos((r2**2-r1**2+d**2)/(2*r2*d))

        s1 = ((r1**2 * (f1 - math.sin(f1)))/2)
        s2 = ((r2**2 * (f2 - math.sin(f2)))/2)

        s = s1 + s2
        return s

    except:
        print("Пожалуйста, проверьте данные")

print(f'Площадь пересечения окружностей - {search_s(d, r1, r2)}')
fig, ax = plt.subplots()
circle1 = plt.Circle((x1, y1), r1, fill = False)
circle2 = plt.Circle((x2, y2), r2, fill = False)
ax.add_artist(circle1)
ax.add_artist(circle2)
plt.grid()
plt.ylim(-7, 15)
plt.xlim(-7, 15)
plt.show()