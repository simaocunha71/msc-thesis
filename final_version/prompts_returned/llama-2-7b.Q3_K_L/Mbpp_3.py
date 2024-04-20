"""
Write a python function to identify non-prime numbers.
assert is_not_prime(2) == False
"""
from typing import Optional, Union

def is_not_prime(num: Union[int, float]):
    if num < 10:
        return True