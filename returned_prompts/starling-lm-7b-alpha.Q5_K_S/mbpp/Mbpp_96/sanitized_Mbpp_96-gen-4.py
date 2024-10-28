from math import sqrt
def divisor(n):
    if n < 0:
        return 0
    c = 0
    for i in range(1, int(sqrt(n)) + 1):
        if n % i == 0:
            c += 1
            if i != n / i:
                c += 1
    return c