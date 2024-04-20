"""
Write a python function to find the sum of even factors of a number.
assert sumofFactors(18) == 26
"""
import math

def sumofFactors(n):
    """ return sum of all even numbers between 2 and n"""

    i = 2; j = n + 1; f = 0
    while i <= j:
        if f == 0: # odd number, skip even factors
            i += 2
        else:
            f -= 1
        if f > 0:
            print(i, end=' ')
            f += 2
        i += 2
    print()
    
sumofFactors(18)