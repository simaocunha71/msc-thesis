
def last_Digit_Factorial(n):
    res = 1
    for i in range(1, n+1):
        res *= i
    return res%10

