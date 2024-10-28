from typing import List


def remove_duplicates(numbers: List[int]) -> List[int]:
    seen = set()
    result = []
    for num in numbers:
        if num not in seen:
            result.append(num)
            seen.add(num)
    return result

# Test cases
print(remove_duplicates([1, 2, 3, 2, 4]))  # [1, 3, 4]
print(remove_duplicates([1, 1, 1, 1, 1]))  # []
print(remove_duplicates([1, 2, 3, 4, 5]))  # [1, 2, 3, 4, 5]
print(remove_duplicates([5, 4, 3, 2, 1]))  # [5, 4, 3, 2, 1]
print(remove_duplicates([1, 2, 2, 3, 3, 4]))  # [1, 4]
print(remove_duplicates([1]))  # [1]
print(remove_duplicates([]))  # []