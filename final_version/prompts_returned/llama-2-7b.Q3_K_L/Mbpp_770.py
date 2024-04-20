"""
Write a python function to find the sum of fourth power of first n odd natural numbers.
assert odd_num_sum(2) == 82
"""
from typing import Optional, Tuple

def odd_num_sum(limit: int=None):
    if limit is None:
        start = 1
    else:
        start = 0
    
    sum: Optional[int] = None
    for i in range(start, limit+1, 2):
        if i%4 == 3: # when we get to (n-1)th number
            sum += i**4
            print('The sum of fourth power of first n odd natural numbers = ' + str(sum))
    return sum