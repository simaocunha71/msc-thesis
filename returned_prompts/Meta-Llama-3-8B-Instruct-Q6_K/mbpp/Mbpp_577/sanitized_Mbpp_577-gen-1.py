def last_Digit_Factorial(n):
    if n == 0:
        return 1
    else:
        return (last_Digit_Factorial(n-1)*n) % 10