from typing import List, Tuple


def rolling_max(numbers: List[int])  -> List[int]:
    max_list = []
    max_num = numbers[0]
    for num in numbers:
        if num > max_num:
            max_num = num
        max_list.append(max_num)
    return max_list

print(rolling_max([1, 2, 3, 2, 3, 4, 2]))

This solution iterates over the list of integers and keeps track of the maximum value found so far, appending it to a new list. When the next number is larger than the current maximum, that number is set as the new maximum.

This solution has a time complexity of O(n) and space complexity of O(n), where n is the length of the input list.
"""

"""
