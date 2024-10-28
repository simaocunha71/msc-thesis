from typing import List

def remove_duplicates(numbers: List[int]) -> List[int]:
    seen = set()
    result = []
    for num in numbers:
        if num not in seen:
            seen.add(num)
            result.append(num)
    return result

# Test the function
print(remove_duplicates([1, 2, 3, 2, 4]))  # Output: [1, 3, 4]
print(remove_duplicates([1, 1, 2, 2, 3]))  # Output: [1, 2, 3]
print(remove_duplicates([1, 2, 3, 4, 5]))  # Output: [1, 2, 3, 4, 5]
print(remove_duplicates([]))  # Output: []


# Code explanation:
# 1. Initialize an empty set `seen` to keep track of elements we have seen.
# 2. Initialize an empty list `result` to store the output.
# 3. Iterate over the input list `numbers`.
# 4. For each number, check if it is not in the `seen` set. If it is not, add it to the `seen` set and append it to the `result` list.
# 5. Return the `result` list.
# 6. The time complexity of this solution is O(n), where n is the length of the input list, because we make a single pass through the list.
# 7. The space complexity is also O(n), as we use a set to keep track of the elements we have seen, which can grow up to the size of the input list in the worst case.