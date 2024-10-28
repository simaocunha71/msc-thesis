from typing import List, Tuple

def rolling_max(numbers: List[int]) -> List[int]:
    max_numbers = [numbers[0]]
    for i in range(1, len(numbers)):
        max_numbers.append(max(numbers[i], max_numbers[i-1]))
    return max_numbers

print(rolling_max([1, 2, 3, 2, 3, 4, 2]))

The function `rolling_max` generates a list of rolling maximum element found until given moment in the sequence. It does this by iterating over the input list `numbers`, and at each position `i`, it checks if the current number is greater than the previous rolling maximum, and if so, it appends the current number to the list `max_numbers`. If the current number is not greater, it appends the previous rolling maximum to the list `max_numbers`.

This solution has a time complexity of O(n), where n is the length of the input list `numbers`.
"""