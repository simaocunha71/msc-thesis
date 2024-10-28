def last_Digit_Factorial(n: int) -> int:
    if n == 0:
        return 1
    return (n * last_Digit_Factorial(n - 1)) % 10

