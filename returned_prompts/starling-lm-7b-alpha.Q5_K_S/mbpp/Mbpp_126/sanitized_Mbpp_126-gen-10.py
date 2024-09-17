from math import gcd
def sum(a, b):
    d = 0
    for i in range(1, int(gcd(a,b)) + 1):
        if a % i == 0 and b % i == 0:
            d += i
    return d