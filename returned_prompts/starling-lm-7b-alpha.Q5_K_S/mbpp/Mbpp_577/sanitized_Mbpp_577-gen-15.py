def last_Digit_Factorial(n):
    if (n == 0):
        return 1
    elif (n % 10 == 0):
        return 0
    else:
        return ((n % 10) * last_Digit_Factorial(n - 1)) % 10