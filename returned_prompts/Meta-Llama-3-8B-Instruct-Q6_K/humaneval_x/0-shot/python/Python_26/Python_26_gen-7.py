from typing import List

def remove_duplicates(numbers: List[int]) -> List[int]:
    seen = set()
    return [num for num in numbers if not (num in seen or seen.add(num))]

# Testing
print(remove_duplicates([1, 2, 3, 2, 4]))  # Output: [1, 3, 4]







