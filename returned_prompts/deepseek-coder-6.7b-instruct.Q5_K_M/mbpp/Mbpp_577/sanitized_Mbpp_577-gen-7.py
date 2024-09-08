def last_Digit_Factorial(n):
    factorial = 1
    for i in range(1, n+1):
        factorial *= i
        while factorial % 10 == 0:
            factorial /= 10
        factorial = int(factorial % 100000)
    return factorial % 10 if factorial else 0