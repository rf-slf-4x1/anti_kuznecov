# Смирнов Дмитрий, 421 группа
# Нахождение НОД методом Евклида

num1 = int(input('Введите первое число: '))
num2 = int(input('Введите второе число: '))

def gcd (num1, num2):
    while num1 != 0 and num2 != 0:
        if num1 >= num2:
            num1 %= num2
        else:
            num2 %= num1
    return num1 or num2

print(f"НОД этих двух чисел: {gcd(num1, num2)}")
