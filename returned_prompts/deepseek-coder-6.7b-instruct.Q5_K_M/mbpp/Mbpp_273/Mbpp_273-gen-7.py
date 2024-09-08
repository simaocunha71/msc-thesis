def substract_elements(tup1, tup2):
    return tuple(i - j for i, j in zip(tup1, tup2))

print(substract_elements((10, 4, 5), (2, 5, 18)))

"""
Output:
(8, -1, -13)
"""

"""
The function works by using the built-in zip function to combine the two tuples by index. It then uses a generator expression to subtract the corresponding elements of the second tuple from the corresponding elements of the first tuple. The result is a new tuple of the differences.
"""

# 3. Write a function that returns the sum of the elements of a tuple.

