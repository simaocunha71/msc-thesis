from typing import List


def rescale_to_unit(numbers: List[float]) -> List[float]:
    min_num = min(numbers)
    max_num = max(numbers)
    return [(n - min_num) / (max_num - min_num) for n in numbers]

print(rescale_to_unit([1.0, 2.0, 3.0, 4.0, 5.0]))

# Output: [0.0, 0.25, 0.5, 0.75, 1.0]

Explanation:
In this function, we first find the minimum and maximum numbers in the given list. The minimum number is subtracted from all numbers, and then the result is divided by the difference between the maximum and minimum. This scales the numbers so that the smallest becomes 0 and the largest becomes 1. The transformed numbers are returned in a new list.

Note: This function assumes that the input list contains at least two elements. If the input list contains less than two elements, the function will raise a ValueError.
"""

# Task 3
"""
