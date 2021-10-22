# Смирнов Дмитрий, 421 группа
# Скрипт генерации простого числа данной длины

from random import *

len_number = int(input('Введите количество цифр в числе: '))
testing = int(input('Введите число проверок: '))

def generator(len_number):
	range_start = 10**(len_number - 1)
	range_end = (10**len_number) - 1
	number = int((str((randint(range_start, range_end))//10)) + (str(choice([1,3,7,9]))))
	return number

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

i = False

while i == False:
    num = generator(len_number)
    if miller_rabin(num, testing) == True:
        i = True
        print(f'Число {num} простое по проверке алгритмом Миллера-Рабина')
    