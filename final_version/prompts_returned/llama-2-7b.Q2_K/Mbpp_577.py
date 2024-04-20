"""
Write a python function to find the last digit in factorial of a given number.
assert last_Digit_Factorial(4) == 4
"""
from math import ceil, log10
def last_digit_factorial(n: int):
    if n < 3:
        return 2**ceil(log10(n)-log10(2))
    else:
        return factorial(n-1)/last_digit_factorial(n-1) - log10(2), 0, n/2
