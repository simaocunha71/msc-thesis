def last_Digit_Factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * last_Digit_Factorial(n - 1) % 10

