def last_Digit_Factorial(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
        while result % 10 == 0:
            result //= 10
        result %= 1000000000
    return result % 10