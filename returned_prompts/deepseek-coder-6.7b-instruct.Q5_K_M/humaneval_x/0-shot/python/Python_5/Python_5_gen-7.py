from typing import List

def intersperse(numbers: List[int], delimeter: int) -> List[int]:
    return [num for i, num in enumerate(numbers) if i != 0 ] + [delimeter] + [num for i, num in enumerate(numbers) if i != len(numbers) - 1]

print(intersperse([], 4))
print(intersperse([1, 2, 3], 4))

This solution creates two lists from the input list `numbers' by excluding the first and last numbers, respectively. These two lists are then combined with the delimeter in between.

The solution uses list comprehension to create the new lists. The enumerate function is used to get the index and value of each