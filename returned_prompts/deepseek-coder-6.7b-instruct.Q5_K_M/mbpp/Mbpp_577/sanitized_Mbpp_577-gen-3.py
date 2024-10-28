def last_Digit_Factorial(n):
    if n == 0:
        return 1
    fact = 1
    for i in range(1, n+1):
        fact *= i
        while fact % 10 == 0:
            fact /= 10
        fact %= 10
    return int(fact % 10)