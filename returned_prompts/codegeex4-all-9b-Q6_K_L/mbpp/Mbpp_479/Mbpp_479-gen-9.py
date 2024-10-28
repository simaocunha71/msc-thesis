def first_Digit(n):
    n = abs(n)
    while n >= 10:
        n /= 10
    return int(n)

