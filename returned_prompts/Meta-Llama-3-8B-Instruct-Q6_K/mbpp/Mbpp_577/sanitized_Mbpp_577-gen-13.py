def last_Digit_Factorial(n):
    if n == 0:
        return 1
    last_digit = 10
    for i in range(1, n + 1):
        last_digit = last_digit % i
    return last_digit