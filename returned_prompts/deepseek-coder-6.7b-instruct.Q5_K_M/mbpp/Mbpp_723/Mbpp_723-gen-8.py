def count_same_pair(l1, l2):
    return sum(x == y for x, y in zip(l1, l2))

print(count_same_pair([1, 2, 3, 4, 5, 6, 7, 8],[2, 2, 3, 1, 2, 6, 7, 9]))

"""
The function works by using the built-in zip function to create a list of pairs of corresponding elements from the input lists. Then, it uses a generator comprehension to create a list of Boolean values indicating whether the corresponding pair of elements in the input lists are equal. Finally, it returns the sum of these Boolean values, which is the number of indices where the lists have the same values.
"""

# Task 2
