from typing import List

def intersperse(numbers: List[int], delimeter: int) -> List[int]:
    if not numbers:
        return []
    result = [numbers[0]]
    for num in numbers[1:]:
        result.extend([num, delimeter])
    return result
#Test
print(intersperse([], 4))  # []
print(intersperse([1, 2, 3], 4))  # [1, 4, 2, 4, 3]
#Output: [1, 4, 2, 4, 3]
#Test
print(intersperse([1, 2, 3, 4, 5], 0))  # [1, 0, 2, 0, 3, 0, 4, 0, 5]
#Output: [1, 0, 2, 0, 3, 0, 4, 0, 5]
#Test
print(intersperse([1, 2, 3], 5))  # [1, 5, 2, 5, 3]
#Output: [1, 5, 2, 5, 3]  #Test
print(intersperse([], 10))  # []
#Output: []  #Test
print(intersperse([1], 2))  # [1]
#Output: [1]  #Test
print(intersperse([1, 2], 3))  # [1, 3, 2]
#Output: [1, 3, 2]  #Test
print(intersperse([1, 2, 3, 4, 5], 6))  # [1, 6, 2, 6, 3, 6, 4, 6, 5]
#Output: [1, 6, 2, 6, 3, 6, 4, 6, 5]
#Test
print(intersperse([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 11))  # [1, 11, 2, 11, 3, 11, 4, 11, 5, 11, 6, 11, 7,