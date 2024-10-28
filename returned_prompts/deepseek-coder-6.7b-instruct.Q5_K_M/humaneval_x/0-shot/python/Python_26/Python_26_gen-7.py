from typing import List

def remove_duplicates(numbers: List[int]) -> List[int]:
    res = []
    for num in numbers:
        if num not in res:
            res.append(num)
    return res

print(remove_duplicates([1, 2, 3, 2, 4]))

"""
This solution uses a list to keep track of the numbers that have already been seen in the input list. It iterates over the input list and if a number has not been seen before, it is appended to the result list.
"""

# Testing
assert remove_duplicates([1, 2, 3, 2, 4]) == [1, 2, 3, 4]
assert remove_duplicates([1, 1, 1, 1, 1]) == [1]
assert remove_duplicates([]) == []
assert remove_duplicates([1, 2, 3, 4, 5]) == [1, 2, 3, 4, 5]
"""
assert remove_duplicates([1, 2, 3, 2, 4]) == [1, 2, 3, 4]
assert remove_duplicates([1, 1, 1, 1, 1]) == [1]
assert remove_duplicates([]) == []
assert remove_duplicates([1, 2, 3, 4, 5]) == [1, 2, 3, 4, 5]
"""
print("All tests passed.")
