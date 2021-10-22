#https://code.activestate.com/recipes/578838-rsa-a-simple-and-easy-to-read-implementation/

import random
from collections import namedtuple
from sympy import primerange
import numpy as np


def get_primes(start, stop):
    primes = [i for i in primerange(start,stop)]
# =============================================================================
#     #Возвращает простые числа в ``диапазоне(start, stop)``.
#     if start >= stop:
#         return []
# 
#     primes = [2]
# 
#     for n in range(3, stop + 1, 2):
#         for p in primes:
#             if n % p == 0:
#                 break
#         else:
#             primes.append(n)
# 
#     while primes and primes[0] < start:
#         del primes[0]
# =============================================================================
    return primes


def are_relatively_prime(a, b):
    #Возвращает ``True`` если ``a`` и ``b`` взаимно простые.
    for n in range(2, min(a, b) + 1):
        if a % n == b % n == 0:
            return False
    return True


def make_key_pair(length):
    """Создаёт публичную-закрытую пару ключей.

    The key pair is generated from two random prime numbers. The argument
    ``length`` specifies the bit length of the number ``n`` shared between
    the two keys: the higher, the better.
    """
    if length < 4:
        raise ValueError('cannot generate a key of length less '
                         'than 4 (got {!r})'.format(length))

    # Первый шаг: поиск числа ``n`` являющегося произведением двух простых чисел
    # числа (``p`` и ``q``). ``n`` должны быть заданной длинны в двоичном коде
    # длинны ``length``, следовательно должны быть в ``диапазоне(n_min, n_max + 1)``.
    n_min = 1 << (length - 1)
    n_max = (1 << length) - 1

    # Ключ сложнее если ``p`` и ``q`` имеют похожую битовую длинну. Мы
    # выбираем два простых числа в ``range(start, stop)`` так что
    # эта разница не превосходит 2.
    start = 1 << (length // 2 - 1)
    stop = 1 << (length // 2 + 1)
    primes = get_primes(start, stop)
    print('primes finded')

    # Теперь мы имеем список кандидатов на простые числа, случайно выбираем
    # два их них в ``range(n_min, n_max + 1)``.
    while primes:
        p = random.choice(primes)
        primes.remove(p)
        q_candidates = [q for q in primes
                        if n_min <= p * q <= n_max]
        if q_candidates:
            q = random.choice(q_candidates)
            break
    else:
        raise AssertionError("cannot find 'p' and 'q' for a key of "
                             "length={!r}".format(length))
    print(1)

    # Далее: выбираем число ``e`` меньше чем ``(p - 1) * (q - 1)``
    # которое не имеет общих делителей ``(p - 1) * (q - 1)``.
    stop = (p - 1) * (q - 1)
    for e in range(3, stop, 2):
        if are_relatively_prime(e, stop):
            break
    else:
        raise AssertionError("cannot find 'e' with p={!r} "
                             "and q={!r}".format(p, q))
    print(2)

    # После: ищем ``d`` такой ``(d * e - 1)`` делиться на
    # ``(p - 1) * (q - 1)``.
    for d in range(3, stop, 2):
        if d * e % stop == 1:
            break
    else:
        raise AssertionError("cannot find 'd' with p={!r}, q={!r} "
                             "and e={!r}".format(p, q, e))
    print(3)

    # Всё, имеем пару ключей.
    return PublicKey(p * q, e), PrivateKey(p * q, d)


class PublicKey(namedtuple('PublicKey', 'n e')):
    """Открытый ключ, который можно использовать для шифрования данных ."""

    __slots__ = ()

    def encrypt(self, x):
        """Шифрование числа ``x``.

        В результате имеем число которое можно расшифровать только закрытым ключём.
        """
        return pow(x, self.e, self.n)


class PrivateKey(namedtuple('PrivateKey', 'n d')):
    """Закрытый ключ, который можно использовать как для дешифрования данных. """

    __slots__ = ()

    def decrypt(self, x):
        """Расшифровка числа ``x``.

        Аргумент x должен быть результатом метода encrypt открытого ключа. 
        """
        return pow(x, self.d, self.n)

import math

def bytes2nums(b, d):
    splitedb = [b[i*d:(i+1)*d] for i in range(math.ceil(len(b)/d))]
    return  [int.from_bytes(b, "big") for b in splitedb]

def nums2bytes(nums):
    splitedb = [num.to_bytes(math.ceil(math.log2(num)/8), byteorder='big') for num in nums]
    return b''.join(splitedb)

if __name__ == '__main__':    
    #получаем пару ключей
    d = 4 # длина ключа в байтах
    public, private = make_key_pair(d*8)
    infile = open('test.txt', 'rb')
    bs = infile.read()
    infile.close()
    
    nums = bytes2nums(bs, d)
    
    encripted = [public.encrypt(n) for n in nums]
    
    encriptedb = nums2bytes(encripted)
    outfile = open('test_encripted.txt', 'wb')
    outfile.write(encriptedb)
    outfile.close()
    
    encripted_ = bytes2nums(encriptedb, d)
    
    decripted = [private.decrypt(n) for n in encripted_]
    
    decriptedb = nums2bytes(decripted)
    outfile = open('test_decripted.txt', 'wb')
    outfile.write(decriptedb)
    outfile.close()
    
    print(nums)
    print(decripted)
    
    