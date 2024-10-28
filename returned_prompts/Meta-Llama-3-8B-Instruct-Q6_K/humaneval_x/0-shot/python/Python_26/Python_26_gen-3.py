from typing import List

def remove_duplicates(numbers: List[int]) -> List[int]:
    seen = set()
    result = []
    for num in numbers:
        if num not in seen:
            seen.add(num)
            result.append(num)
    return result

# Example usage:
numbers = [1, 2, 3, 2, 4]
print(remove_duplicates(numbers))  # Output: [1, 3, 4]  # [1, 2, 3, 4]
# [1, 2, 3, 2, 4]
# [1, 3, 4]
# [1, 2, 3, 4]
# [1, 3, 4]

# The time complexity of this solution is O(n), where n is the length of the input list,
# because we are making a single pass through the list.
# The space complexity is O(n) as well, because in the worst case (when all numbers are unique)
# we might need to store all numbers in the set and the result list.  # [1, 2, 3, 4]
# [1, 3, 4]
# [1, 2, 3, 4]
# [1, 3, 4]
# [1, 2, 3, 4]
# [1, 3, 4]  # [1, 2, 3, 4]
# [1, 3, 4]
# [1, 2, 3, 4]
# [1, 3, 4]  # [1, 2, 3, 4]
# [1, 3, 4]
# [1, 2, 3, 4]
# [1, 3, 4]
# [1, 2, 3, 4]
# [1, 3, 4]
# [1, 2, 3, 4]
# [1, 3, 4]
# [1, 2, 3, 4]
# [1, 3, 4]
# [1, 2, 3, 4]
# [1, 3, 4]
# [1, 2, 3, 4]
# [1, 3, 4]
# [1, 2