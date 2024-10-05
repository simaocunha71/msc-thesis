from typing import List

def intersperse(numbers: List[int], delimeter: int) -> List[int]:
    result = []
    for i in range(len(numbers)):
        result.append(numbers[i])
        if i < len(numbers) - 1:
            result.append(delimeter)
    return result

# Test cases
print(intersperse([], 4))  # []
print(intersperse([1, 2, 3], 4))  # [1, 4, 2, 4, 3]

The function intersperse takes a list of integers and an integer as input. It creates a new list where the original list is interspersed with the delimiter integer between each pair of elements. If the original list is empty, it returns an empty list.
"""
