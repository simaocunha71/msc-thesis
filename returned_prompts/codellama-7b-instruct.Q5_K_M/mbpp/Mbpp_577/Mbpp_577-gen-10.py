def last_Digit_Factorial(n):
    result = 1
    for i in range(2, n+1):
        result *= i
    return result % 10
