"""
Write a python function to find even numbers from a list of numbers.
assert Split([1,2,3,4,5]) == [2,4]
"""
from typing import Any
def split(numbers: Any) -> Any:
    number = 0
    for i in numbers:
        if (i + 1) % 2 == 0:
            number += 1
    return number
