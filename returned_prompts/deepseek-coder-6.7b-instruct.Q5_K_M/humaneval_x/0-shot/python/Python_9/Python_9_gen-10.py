from typing import List, Tuple

def rolling_max(numbers: List[int]) -> List[int]:
    max_val = numbers[0]
    res = [max_val]
    for num in numbers[1:]:
        if num > max_val:
            max_val = num
        res.append(max_val)
    return res

print(rolling_max([1, 2, 3, 2, 3, 4, 2]))


# Output:
# [1, 2, 3, 3, 3, 4, 4]

Explanation:
The function iterates over the input list. For each number, it compares it with the current max_value. If the number is greater than max_value, it updates the max_value to the number. Then it appends the new max_value to the result list.
"""

