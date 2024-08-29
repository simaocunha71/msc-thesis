def count_same_pair(list1, list2):
    return sum(1 for a, b in zip(list1, list2) if a == b)

print(count_same_pair([1, 2, 3, 4, 5, 6, 7, 8],[2, 2, 3, 1, 2, 6, 7, 9])) # Output: 4

"""
Explanation:
The function `count_same_pair` takes two lists as input and returns the number of indices where the values at these indices are the same in both lists.
We use the `zip` function to iterate over the two lists simultaneously, and the `sum` function with a generator to count the indices where the two values are the same.
"""

"""
