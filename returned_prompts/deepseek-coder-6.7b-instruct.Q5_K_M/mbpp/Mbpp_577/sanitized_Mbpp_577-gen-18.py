def last_Digit_Factorial(n):
    if n == 0:
        return 1
    else:
        fact = 1
        for i in range(1, n + 1):
            fact = (fact * i) % 10
        return fact