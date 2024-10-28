def last_Digit_Factorial(n: int) -> int:
    return factorial(n) % 10
def factorial(n: int) -> int:
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n-1)