def first_Digit(n):
    while n >= 10:
        n //= 10
    return n