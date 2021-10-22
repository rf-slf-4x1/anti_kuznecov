from random import randint, choice

N = int(input("Сколько знаков должно быть в числе: "))
number_of_checks = int(input("Сколько тестов Миллера должно быть проведено: "))

def generator(n):
    range_start = 10**(n-1)
    range_end = (10**n)-1
    number = int((str((randint(range_start, range_end))//10)) + (str(choice([1,3,7,9]))))
    return number

def test(N, number_of_checks):
    for i in range(2, 2 + number_of_checks):
        if pow(i, ((N-1)/2), N) != 1    : return False
    return True

def test_millera(N, number_of_checks):
    s = 0

    for i in range (N):
        if (N - 1) % (2**i) == 0:
            s = i
        else: break

    d = int((N-1)/(2**s))
    for a in range (2, 2 + number_of_checks):
        f = False
        if pow(a, d, N) == 1:
            f = True
        for r in range (1, s):
            if (a, 2**r*d, N) == (-1):
                f = True

        if not f:
            return False

    return True

num = generator(N)

while not test_millera(num, number_of_checks):
    num = generator(N)
print(f"Простое число из {N} цифр - {num}")
