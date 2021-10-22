# Смирнов Дмитрий, 421 группа
# Скрипт для проверки факта, является ли число - числом Кармайкла

number = int(input('Введите число: '))

def gcd (num1, num2):
    while num1 != 0 and num2 != 0:
        if num1 >= num2:
            num1 %= num2
        else:
            num2 %= num1
    return num1 or num2

# def isCarmichaelNumber(number):
    
#     for b in range(2, number):
        
#         if gcd (b, number) == 1:

#             if pow (b, number - 1, number) != 1:
#                 return False
            
#     return True

def isCarmichaelNumber(number) :
    b = 2
    while b < number:
         
        if (gcd (b, number) == 1):
 
            if (pow(b, number - 1, number) != 1):
                return False
        b = b + 1
    return True

# def isCarmichaelNumber(number):
#     for i in range(2, number):
#         if gcd(i, number) == 1:
#             if pow(i, number - 1, number) != 1:
#                 return False
#     return True

if isCarmichaelNumber(number) == True:
    print('Это число Кармайкла')

else:
    print('Число не является числом Кармайкла')