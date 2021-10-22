from sympy import primerange, isprime
from random import randint, choice
import numpy as np

#проверка на простоту
def test_ferma(n, countA):
    for i in range(2,2+countA):
        if pow(i, n-1, n) != 1: return False
    return True

def test_millrab(n, countA):
    s = 0
    for i in range(n):
        if (n-1) % (2**i) == 0:
            s = i
        else: break
    d = int((n-1) / (2**s))
    for i in range(countA):
        a = randint(1, n-1)
        f = False
        #первое условие
        if pow(a,d,n) == 1:
            f = True
            break
        if f: break
        #второе условие
        for r in range(s):
            if pow(a,2**r*d,n) == -1:
                f = True
                break
        if not f: return False
    return True

def gen(n):
    return randint(10**(n-2), (10**(n-1))-1)*10+choice([1,3,7,9])


def gen_gen_prime(n, countA, test):
    num = gen(n)
    i = 0
    while not test(num, countA): # генерим пока не нагенерим)
        num = gen(n)
        i += 1 # счётчик считающий количество попыток
    return num

n = 19 # длинна числа
countA = 1 # количество тестов


print(gen_gen_prime(n, countA, test_millrab))