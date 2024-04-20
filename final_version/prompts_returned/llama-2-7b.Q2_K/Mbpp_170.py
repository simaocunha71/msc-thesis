"""
Write a function to find the sum of numbers in a list within a range specified by two indices.
assert sum_range_list([2,1,5,6,8,3,4,9,10,11,8,12], 8, 10) == 29
"""
import math
from typing import List

def sum_range(num:int, start:int, end:int):
    """Define function to find the sum of numbers in a list within a range specified by two indices."""
    return sum([i for i in range(start, end + 1) if num > 0 and (num & 1) == 0])

def sum_range_list(numbers:List[int], start:int, end:int):
    """Define function to find the sum of numbers in a list within a range specified by two indices."""
    return sum([sum_range(i, i + 1) for i in range(start - 1, end + 2)])