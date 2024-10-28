def power(a, b):
    result = 1
    while b > 0:
        if b % 2 == 1:
            result *= a
        b >>= 1
        a *= a
    return result