"""
Write a function to get the sum of the digits of a non-negative integer.
assert sum_digits(345)==12
"""
from typing import Optional

def sum_digits(num: int = 10, start=0):
    i = start
    cnt = 0
    
    while num > 0:
        cnt += 1
        i += 1
        
        if num % i == 0:
            cnt += num // i
        else:
            break
            
    return cnt
