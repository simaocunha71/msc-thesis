def two_unique_nums(nums):
    return list(set(nums))

print(two_unique_nums([1,2,3,2,3,4,5]))

# Output: [1, 2, 3, 4, 5]

"""
Explanation:
The function `two_unique_nums` takes a list of numbers as its argument.
It first converts the list to a set, which automatically removes all duplicate numbers.
Then it converts the set back to a list and returns it.
The order of the numbers in the list may vary as sets are unordered in Python.
"""

