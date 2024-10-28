from typing import List

def remove_duplicates(numbers: List[int]) -> List[int]:
    non_duplicates = []
    for num in numbers:
        if num not in non_duplicates:
            non_duplicates.append(num)
    return non_duplicates

print(remove_duplicates([1, 2, 3, 2, 4]))


# Alternatively, we can use a dictionary to keep track of the elements that have been encountered.
# This is faster as lookup in dictionary is faster than in a list.

def remove_duplicates(numbers: List[int]) -> List[int]:
    encountered = {}
    non_duplicates = []
    for num in numbers:
        if num not in encountered:
            encountered[num] = 1
            non_duplicates.append(num)
    return non_duplicates

print(remove_duplicates([1, 2, 3, 2, 4]))

# Both of these solutions have O(n) time complexity where n is the length of the list.

# Note: The order of elements in the output is the same as in the input.

# The first solution uses the append method which has O(n) complexity in the worst case.
# So, it's more efficient to use a dictionary to check if a number has been encountered or not.
# The dictionary operations (add, get) are O(1) on average.

# If the order of elements is not important, we can sort the list first,
# then iterate through the list to remove duplicates. This will be faster, but the order of elements will be changed.

# Also, if the numbers are within a certain range, we can use a bit manipulation trick to remove duplicates,
# but it's not applicable if the numbers are negative or are not integers.

# These solutions are good enough for most cases, but they might be slow for very large inputs.
# In that case, you might want to use a different data structure, like a set or a sorted list,
# or use a library that implements these operations more efficiently.

# If the list is sorted, we can also use two po