def last_Digit_Factorial(n):
    last_digit = 1
    for i in range(1, n+1):
        last_digit = (last_digit * i) % 10
    return last_digit