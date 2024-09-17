def last_Digit_Factorial(n):
    if n == 0:
        return 1
    elif n == 1:
        return 1
    elif n == 2:
        return 2
    else:
        return (n * last_Digit_Factorial(n - 1)) % 10