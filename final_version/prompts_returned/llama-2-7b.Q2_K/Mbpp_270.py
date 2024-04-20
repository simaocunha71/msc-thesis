"""
Write a python function to find the sum of even numbers at even positions of a list.
assert sum_even_and_even_index([5, 6, 12, 1, 18, 8]) == 30
"""
from typing import Optional

def sum_even_and_even_index(nums: [Optional[int]]) -> int:
    """
    List comprehension to get the length of nums and then convert it into a list.
    Loop over even numbers and even index positions in each iteration. The inner loop iterates over only elements at odd indexes 
    which are even numbers.
    
    Example output of the above code:
    >>> sum_even_and_even_index([5, 6, 12, 1, 18, 8])
        30
    """
    length = len(nums)
    even_numbers = [i for i in range(length) if (i % 2 == 0)]
    indexes = [i for i in range(length) if (i % 2 != 0 and i >= 0)]
    
    return sum([even[i]**2+even[i]*indexes[i] for even, index in zip(even_numbers, indexes)])
