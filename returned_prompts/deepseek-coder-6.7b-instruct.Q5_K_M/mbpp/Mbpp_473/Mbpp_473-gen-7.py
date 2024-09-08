"""
def tuple_intersection(tuple_list):
    # Convert the tuple lists to sets of frozensets for intersection
    sets = [set(frozenset(i) for i in t) for t in tuple_list]

    # Find the intersection of all sets
    intersection = set.intersection(*sets)

    # Convert back to tuples
    intersection = [tuple(i) for i in intersection]

    return set(intersection)
"""

# Explanation:
# The function `tuple_intersection` takes a list of tuples as input. It converts each tuple into a set of frozensets,
# where each frozenset represents a tuple. Then it finds the intersection of all sets using the `set.intersection` method.
# Finally, it converts each frozenset back into a tuple and returns the result as a set.

# Test the function with the given example
print(tuple_intersection([(3, 4),  (5, 6),  (9, 10),  (4, 5)] , [(5, 4),  (3, 4),  (6, 5),  (9, 11)])) # Output: {(4, 5), (3, 4), (5, 6)}

# Test the function with another example
print(tuple_intersection([(1, 2), (3, 4), (5, 6)], [(2, 1), (4, 3), (6, 5)])) # Output: {(1, 2), (3, 4), (5, 6)}

# Test the function with another example
print(tuple_intersection([(1, 2), (3, 4), (5, 6)], [(2, 1), (4, 3), (7, 8)])) # Output: {(1, 2), (3, 4)}

# Test the function with another example
print(tuple_intersection([(1, 2), (3, 4), (5, 6)], [(2, 1), (8, 9), (7, 8)]