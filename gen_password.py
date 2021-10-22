# =============================================================================
# Сгенерировать пароль для пользователя.
# Требования:
#     6-20 символов
#     1 символ подчёркивания
#     >= 2х заглавных букв
#     не более 5 цифр
#     2 цифры подряд недопустимы
# =============================================================================

import random
let='qwertyuiopasdfghjklzxcvbnm'.upper()
simbols='qwertyuiopasdfghjklzxcvbnm!@#$%^&*()-=\|/.,?*-~`"<>[]{}'+let
numbers='1234567890'

#генерируем минимальный набор символов по требованиям
passsimbols = ['_']
numnumbers = random.randint(0,5)
for _ in range(numnumbers):
    passsimbols.append(random.choice(numbers))
passsimbols.append(random.choice(let))
passsimbols.append(random.choice(let))
#теперь добавляем минимальное количество символов чтобы было что ставить между цифрами или чтобы добить минимальное количество символов
#сейчас у нас уже _, две заглавные и numnumbers цифр
l = random.randint(max(6-len(passsimbols), numnumbers-1), 20-len(passsimbols))
for _ in range(l):
    passsimbols.append(random.choice(simbols))

#проверка на соседние цифры (валидность пароля)
def check(ps):
    for i in range(len(ps)-1):
        if ps[i].isnumeric() and ps[i+1].isnumeric(): return False
    return True

while True:
    random.shuffle(passsimbols) # случайным образом мешаем
    if check(passsimbols): break # если проверку прошёл, то вот он наш пароль

password = ''.join(passsimbols)
print(f'new password: {password}')