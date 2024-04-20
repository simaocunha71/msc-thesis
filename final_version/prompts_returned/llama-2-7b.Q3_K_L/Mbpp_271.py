"""
Write a python function that takes in an integer n and finds the sum of the first n even natural numbers that are raised to the fifth power.
assert even_Power_Sum(2) == 1056
"""
from math import factorial, sqrt

def even_Power_Sum(n: int = None):
    """
    even_Power_Sum(num) --> nth sum of first n even natural numbers raised to the fifth power.
    """
    if n is None:
        n = 10 # set a default value when none is passed in
    
    result = 1
    
    for x in range(n+1):
        if (x % 2 == 0 and sqrt(x) != int(sqrt(x))):
            result *= factorial(x)/pow(factorial((int(sqrt(x)))),5)*pow(factorial((int(sqrt(x)))-1),4)
        else:
            break
    
    return result