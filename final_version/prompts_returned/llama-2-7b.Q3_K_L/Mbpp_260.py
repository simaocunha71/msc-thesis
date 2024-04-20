"""
Write a function to find the nth newman–shanks–williams prime number.
assert newman_prime(3) == 7
"""
import math
from typing import List, Optional

def newman_prime(start: int = 100):
    """
    Write a function that finds the nth Newman-Shanks-Williams prime number.
    
    >>> start = 100
    >>> print(newman_prime(start))
    >>> 2993751
    """
    if start == 100: return -1
    for i in range(1, int(math.floor((log(start) / log(2))+1)):
        if newman_prime(i*2) > start:
            break
        else:
            start += i