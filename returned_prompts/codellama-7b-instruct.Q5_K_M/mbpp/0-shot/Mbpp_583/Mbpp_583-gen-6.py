"""
from itertools import combinations
from math import factorial

def catalan_number(n):
    return sum(factorial(2*i)//(factorial(i)*factorial(i+1)) for i in range(n))
"""
