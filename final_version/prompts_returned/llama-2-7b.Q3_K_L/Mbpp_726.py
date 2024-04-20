"""
Write a function that takes as input a tuple of numbers (t_1,...,t_{N+1}) and returns a tuple of length N where the i-th element of the tuple is equal to t_i * t_{i+1}.
assert multiply_elements((1, 5, 7, 8, 10)) == (5, 35, 56, 80)
"""
from typing import List

def multiply_elements(t:List[int]):
    result = []
    for i in t:
        for j in reversed(range(i+1, len(t))):
            result.append(t[i]*t[j])
    return result