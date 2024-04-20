"""
Write a function to calculate the value of 'a' to the power 'b'.
assert power(3,4) == 81
"""
from typing import Union

def power(x: Union[int, float], n: int = 0):
    if x is None or n is None: return None
    res = 1
    for i in range(n + 1):
        res *= x
    return res