def remove_duplicates(numbers: List[int]) -> List[int]:
    counts = {}
    for num in numbers:
        if num in counts:
            counts[num] += 1
        else:
            counts[num] = 1
    return [num for num in counts if counts[num] == 1]

print(remove_duplicates([1, 2, 3, 2, 4]))  # [1, 3, 4]

Explanation:
We create a dictionary to count the occurrence of each number in the list. Then we return a list of numbers that occur exactly once in the list. The order of the numbers in the returned list will be the same as the order in the input list because we are iterating over the numbers in the input list.

The time complexity of this solution is O(n), where n is the number of elements in the list.
The space complexity of this solution is O(n), because we are storing the counts of each number in the list in a dictionary.
"""

# Code:
def remove_duplicates(numbers: List[int]) -> List[int]:
    counts = {}
    for num in numbers:
        if num in counts:
            counts[num] += 1
        else:
            counts[num] = 1
    return [num for num in counts if counts[num] == 1]

print(remove_duplicates([1, 2, 3, 2, 4]))  # [1, 3, 4]

# Test Cases:
assert remove_duplicates([1, 2, 3, 2, 4]) == [1, 3, 4]
assert remove_duplicates([1, 1, 1, 2, 2, 2]) == []
assert remove_duplicates([1, 2, 3, 3, 4, 4, 5]) == [1, 2, 5]
assert remove_duplicates([10, 20, 30, 20, 10, 30, 40]) == [40]
assert remove_duplicates([]) == []

print("