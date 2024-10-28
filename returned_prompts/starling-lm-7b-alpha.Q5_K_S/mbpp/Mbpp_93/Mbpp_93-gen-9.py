
def power(a, b):
    res = 1
    while b > 0:
        if b % 2 != 0:
            res = res * a
        a = a * a
        b = b >> 1
    return res


