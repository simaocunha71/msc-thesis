import re
def first_Digit(n):
    n = abs(n)
    while n > 0:
        digit = n % 10
        n = n // 10
        return digit
    return None