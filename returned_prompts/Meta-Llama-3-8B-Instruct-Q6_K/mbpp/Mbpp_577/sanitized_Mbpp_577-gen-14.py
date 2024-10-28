def last_Digit_Factorial(n):
    if not isinstance(n, int):
        raise ValueError("Input must be an integer")
    if n <= 0:
        return 1
    else:
        return last_Digit_Factorial(n-1) * (n % 10)