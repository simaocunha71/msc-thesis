def last_Digit_Factorial(n):
    if n == 0 or n == 1:
        return 1
    last_digit = 1
    for i in range(2, n+1):
        last_digit *= i
        last_digit %= 10
    return last_digit