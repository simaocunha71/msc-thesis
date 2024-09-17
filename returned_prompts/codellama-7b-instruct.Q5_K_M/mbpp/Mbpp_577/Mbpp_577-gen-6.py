
def last_Digit_Factorial(n: int) -> int:
    fact = 1
    while n > 0:
        fact *= n
        n -= 1
    return fact % 10


