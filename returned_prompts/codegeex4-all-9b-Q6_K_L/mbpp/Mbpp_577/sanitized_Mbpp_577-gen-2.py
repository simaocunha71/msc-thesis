def last_Digit_Factorial(n):
    if n == 0:
        return 1
    else:
        return n * last_Digit_Factorial(n-1) % 10