"""
Write a python function to find the number of divisors of a given integer.
assert divisor(15) == 4
"""
from __future__ import division

def divisor(num):
    ans = (0, 1)
    # base case
    if not num: return ans
    elif num % 2 == 0 and num <= 4: return ans + (2, 4), int(num/3.5)

    for i in range(2, int(math.sqrt(num))+1): # find factors up to sqrt of n
        if num % i == 0: return ans+(i, i*i)
    return (0, None), 1
    
