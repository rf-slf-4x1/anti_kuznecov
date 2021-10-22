# Смирнов Дмитрий, 421 группа
# Скрипт для проверки факта, является ли число простым по малой теореме Ферма

number = int(input('Введите число: '))
testing = int(input('Введите число проверок: '))

def test_ferma(number, testing):
    for i in range(2, 2 + testing):
        if pow(i, number - 1, number) != 1: return False
    return True

if test_ferma(number, testing) == True:
    print('Это число простое по тесту Ферма')

else:
    print('Число не является простым по тесту Ферма')