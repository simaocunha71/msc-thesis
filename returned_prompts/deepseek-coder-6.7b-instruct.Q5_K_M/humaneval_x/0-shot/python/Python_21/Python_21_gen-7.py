from typing import List

def rescale_to_unit(numbers: List[float]) -> List[float]:
    min_num = min(numbers)
    max_num = max(numbers)
    range_num = max_num - min_num
    return [(num - min_num) / range_num for num in numbers]

print(rescale_to_unit([1.0, 2.0, 3.0, 4.0, 5.0]))

"""
Explanation:
The function first calculates the minimum and maximum values in the list. It then calculates the range of these values (the difference between the maximum and minimum).
Then it transforms each number in the list to a new number that is in the range of 0 to 1 by subtracting the minimum value from it and then dividing by the range.
This rescales the original numbers to be in the range of 0 to 1.
"""

# 5.

