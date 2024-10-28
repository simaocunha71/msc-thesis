from typing import List


def remove_duplicates(numbers: List[int])  -> List[int]:
    unique_numbers = []
    for number in numbers:
        if number not in unique_numbers:
            unique_numbers.append(number)
    return unique_numbers


print(remove_duplicates([1, 2, 3, 2, 4]))  # [1, 2, 3, 4]


This solution works by creating a new list unique_numbers. It iterates over each number in the input list numbers. If a number is not already in unique_numbers, it adds it. The end result is a list with all duplicates removed, keeping the original order of elements.
"""

# 2
"""
