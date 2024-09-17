from math import factorial
def last_Digit_Factorial(x):
    # if x is less than 0, return 1
    if x < 0:
        return 1
    # get the factorial of x
    factorial_x = factorial(x)
    # find the last digit of factorial_x
    last_digit = factorial_x % 10
    return last_digit