from typing import List

def has_close_elements(numbers: List[float], threshold: float) -> bool:
    sorted_numbers = sorted(numbers)
    
    for i in range(1, len(sorted_numbers)):
        if sorted_numbers[i] - sorted_numbers[i - 1] < threshold:
            return True
    
    return False

print(has_close_elements([1.0, 2.0, 3.0], 0.5))  # False
print(has_close_elements([1.0, 2.8, 3.0, 4.0, 5.0, 2.0], 0.3))  # True

In the provided solution, we first sort the given list of numbers. Then, we iterate through the sorted list and check if the difference between any two consecutive numbers is less than the given threshold. If we find such a pair, we return True. If we don't find any such pair after iterating through the entire list, we return False.

The time complexity of this solution is O(n log n) due to the sort operation. The space complexity is O(n) because we are storing a sorted copy of the input list.

This solution works for any given list of numbers and any given threshold.
"""

#tests/test_closest_numbers.py
import pytest
from closest_numbers import has_close_elements


def test_has_close_elements():
    assert has_close_elements([1.0, 2.0, 3.0], 0.5) == False
    assert has_close_elements([1.0, 2.8, 3.0, 4.0, 5.0, 2.0], 0.3) == True
    assert has_close_elements([1.0, 2.0, 3.0, 4.0, 5.0], 0.1) == False
    assert has_close_elements([1.0, 2.0, 3.0, 4.0, 5.0], 0.5) == True
    assert has_close_elements([1