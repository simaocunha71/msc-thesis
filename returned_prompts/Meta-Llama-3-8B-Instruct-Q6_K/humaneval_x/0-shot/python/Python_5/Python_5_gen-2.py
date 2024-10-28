from typing import List

def intersperse(numbers: List[int], delimeter: int) -> List[int]:
    result = []
    for i in range(len(numbers)):
        result.append(numbers[i])
        if i < len(numbers) - 1:
            result.append(delimeter)
    return result

# Test cases:
print(intersperse([], 4))  # []
print(intersperse([1, 2, 3], 4))  # [1, 4, 2, 4, 3]
print(intersperse([1, 2, 3, 4], 5))  # [1, 5, 2, 5, 3, 5, 4]  # [1, 5, 2, 5, 3, 5, 4]
print(intersperse([1, 2, 3, 4, 5], 6))  # [1, 6, 2, 6, 3, 6, 4, 6, 5]  # [1, 6, 2, 6, 3, 6, 4, 6, 5]
print(intersperse([], 7))  # []  # []  # []  # []  # []
print(intersperse([1, 2, 3], 4))  # [1, 4, 2, 4, 3]  # [1, 4, 2, 4, 3]  # [1, 4, 2, 4, 3]
print(intersperse([1, 2, 3, 4, 5], 6))  # [1, 6, 2, 6, 3, 6, 4, 6, 5]  # [1, 6, 2, 6, 3, 6, 4, 6, 5]  # [1, 6, 2, 6, 3, 6, 4, 6, 5]  # [1, 6, 2, 6, 3, 6, 4, 6, 5]  # [1, 6, 2, 6, 3, 6, 4, 6, 5] 