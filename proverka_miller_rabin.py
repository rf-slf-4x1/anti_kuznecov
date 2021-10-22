# Смирнов Дмитрий, 421 группа
# Скрипт для проверки числа на простоту методом Миллера-Рабина

from random import *

number = int(input('Введите число: '))
testing = int(input('Введите число проверок: '))

def miller_rabin(number, testing):
	if number == 2:
		return True
	if not number & 1:
		return False

	def check(a, s, d, number):
		x = pow(a, d, number)
		if x == 1:
			return True
		for i in range(s - 1):
			if x == number - 1:
				return True
			x = pow(x, 2, number)
		return x == number - 1

	s = 0
	d = number - 1

	while d % 2 == 0:
		d >>= 1
		s += 1

	for i in range(testing):
		a = randrange(2, number - 1)
		if not check(a, s, d, number):
			return False
	return True

if miller_rabin(number, testing) == True:
    print('Число простое по проверке алгритмом Миллера-Рабина')

else:
    print('Число не является простым по проверке Миллера-Рабина')
