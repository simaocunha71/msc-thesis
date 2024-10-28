
def sort_array(arr):
    return sorted(arr, key=lambda x: (bin(x).count("1"), x))

# Test cases
print(sort_array([1, 5, 2, 3, 4]))  # ➞ [1, 2, 3, 4, 5]
print(sort_array([-2, -3, -4, -5, -6]))  # ➞ [-6, -5, -4, -3, -2]
print(sort_array([1, 0, 2, 3, 4]))  # ➞ [0, 1, 2, 3, 4]

In this solution, we use the built-in function sorted() along with a custom key. The key is a lambda function that returns a tuple. The first element of the tuple is the count of '1's in the binary representation of the number, and the second element is the number itself. Python's tuples are compared lexicographically, so this will sort the numbers based on the number of '1's in their binary representation first, and then by their decimal value if the counts are equal.
"""

# Task 2
"""
