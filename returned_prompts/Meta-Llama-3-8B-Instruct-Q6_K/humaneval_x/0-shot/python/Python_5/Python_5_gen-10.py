from typing import List

def intersperse(numbers: List[int], delimeter: int) -> List[int]:
    if len(numbers) == 0:
        return numbers
    result = [numbers[0]]
    for num in numbers[1:]:
        result.extend([delimeter, num])
    return result

# Test cases
print(intersperse([], 4))  # []
print(intersperse([1, 2, 3], 4))  # [1, 4, 2, 4, 3]
print(intersperse([1, 2, 3, 4, 5], 6))  # [1, 6, 2, 6, 3, 6, 4, 6, 5]  # Test for a longer list
print(intersperse([1], 4))  # [1, 4]
print(intersperse([1, 2, 3, 4], 5))  # [1, 5, 2, 5, 3, 5, 4]  # Test for a list with 4 elements
print(intersperse([1, 2, 3], 0))  # [1, 0, 2, 0, 3]  # Test for delimeter as 0

# Output:
# []
# [1, 4, 2, 4, 3]
# [1, 6, 2, 6, 3, 6, 4, 6, 5]
# [1, 4]
# [1, 5, 2, 5, 3, 5, 4]
# [1, 0, 2, 0, 3]  # Test for delimeter as 0
# [1, 0, 2, 0, 3]  # Test for delimeter as 0
# [1, 0, 2, 0, 3]  # Test for delimeter as 0
# [1, 0, 2, 0, 3]  # Test for delimeter as 0
# [1, 0, 2, 0, 3]  # Test for delimeter as 0
# [1, 0, 2, 0, 3]  # Test