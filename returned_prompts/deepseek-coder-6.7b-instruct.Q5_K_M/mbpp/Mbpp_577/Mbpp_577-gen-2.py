def last_Digit_Factorial(n):
    fact = 1
    for i in range(1, n+1):
        fact *= i
    return fact % 10

print(last_Digit_Factorial(4)) # 4


