def find_dissimilar(t1, t2):
    return tuple(set(t1) ^ set(t2))

assert find_dissimilar((3, 4, 5, 6), (5, 7, 4, 10)) == (3, 6, 7, 10)

Explanation:
The ^ operator in Python performs symmetric difference operation. It returns a set that contains all items from both sets, but not the items present in both sets.
"""

def find_dissimilar(t1, t2):
    return tuple(set(t1).symmetric_difference(set(t2)))

assert find_dissimilar((3, 4, 5, 6), (5, 7, 4, 10)) == (3, 6, 7, 10)
"""

