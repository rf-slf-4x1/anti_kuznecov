# Смирнов Дмитрий, 421 группа
# Скрипт для факторизации числа

number = int(input('Введите число: '))

def factorization(number):

   i = 2
   list = []
   while i * i <= number:
       while number % i == 0:
           list.append(int(i))
           number = number / i
       i = i + 1
   if number > 1:
       list.append(int(number))
   return list

print(factorization(number))