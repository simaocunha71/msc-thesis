from typing import List


def intersperse(numbers: List[int], delimeter: int)  -> List[int]:
    result = []
    for idx, num in enumerate(numbers):
        result.append(num)
        if idx < len(numbers) - 1:
            result.append(delimeter)
    return result


# test cases
print(intersperse([], 4))  # []
print(intersperse([1, 2, 3], 4))  # [1, 4, 2, 4, 3]


The function intersperse receives a list of integers and a delimiter integer as parameters. It then iterates through the list, appending each number and the delimiter to the result list, except for the last number. The result is returned.

The function uses the enumerate function to get both the index and value of the current number being examined in the list. If the index is less than the length of the list minus 1 (i.e., not the last element), it appends the delimiter to the result list.

This way, the delimiter is inserted between every two consecutive elements of the list.

The function returns an empty list if the input list is also empty.
"""

#Task 2
"""
