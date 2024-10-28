from typing import List

def intersperse(numbers: List[int], delimeter: int) -> List[int]:
    result = []
    for i in range(len(numbers)):
        result.append(numbers[i])
        if i < len(numbers) - 1:
            result.append(delimeter)
    return result

# test cases
print(intersperse([], 4))  # []
print(intersperse([1, 2, 3], 4))  # [1, 4, 2, 4, 3]
print(intersperse([1, 2, 3, 4, 5], 0))  # [1, 0, 2, 0, 3, 0, 4, 0, 5]  # 5 0 2 0 3 0 4 0 5
print(intersperse([1], 2))  # [1]
print(intersperse([1, 2], 3))  # [1, 3, 2]  # 1 3 2
print(intersperse([1, 2, 3, 4, 5, 6], 7))  # [1, 7, 2, 7, 3, 7, 4, 7, 5, 7, 6]  # 1 7 2 7 3 7 4 7 5 7 6
print(intersperse([1, 2], 0))  # [1, 0, 2]  # 1 0 2
print(intersperse([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 0))  # [1, 0, 2, 0, 3, 0, 4, 0, 5, 0, 6, 0, 7, 0, 8, 0, 9, 0, 10]  # 1 0 2 0 3 0 4 0 5 0 6 0 7 0 8 0 9 0 10
print(intersperse([1], 1))  # [1]
print(intersperse([1, 2, 3,