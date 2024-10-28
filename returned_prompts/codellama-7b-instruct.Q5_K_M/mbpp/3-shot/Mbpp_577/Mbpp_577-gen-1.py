
def last_Digit_Factorial(n):
    if n == 0 or n == 1 or n == 6 or n == 8 or n == 9:
        return n
    else:
        return last_Digit_Factorial(n // 10)


