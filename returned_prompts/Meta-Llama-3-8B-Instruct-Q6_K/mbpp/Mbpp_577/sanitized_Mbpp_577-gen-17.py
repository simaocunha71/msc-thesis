def last_Digit_Factorial(n):
    if n == 0:
        return 1
    else:
        last_digit = last_Digit_Factorial(n-1)
        return last_digit % 10