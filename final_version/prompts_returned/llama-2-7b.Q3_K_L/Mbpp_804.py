"""
Write a function to check whether the product of numbers in a list is even or not.
assert is_product_even([1,2,3])
"""
from typing import List

def is_product_even(numbers: List[int]):
    assert len(numbers) > 0
    if all(n % 2 == 0 for n in numbers) or sum(numbers)%2==0:
        return True
    else:
        return False