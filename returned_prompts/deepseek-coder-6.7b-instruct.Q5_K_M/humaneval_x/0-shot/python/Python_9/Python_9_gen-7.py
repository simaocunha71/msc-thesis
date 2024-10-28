from typing import List, Tuple

def rolling_max(numbers: List[int]) -> List[int]:
    max_val = numbers[0]
    result = []
    for num in numbers:
        max_val = max(max_val, num)
        result.append(max_val)
    return result

print(rolling_max([1, 2, 3, 2, 3, 4, 2]))

"""
In this function, we initialize the maximum value found so far (`max_val`) to the first number in the list. We also create an empty list (`result`) to store our results. We then iterate over each number in the list. If the current number is greater than the current maximum value, we update `max_val` to this new number. After that, we append `max_val` to `result`. When the loop is done, `result` will contain the rolling maximums.
"""

# 3.11

