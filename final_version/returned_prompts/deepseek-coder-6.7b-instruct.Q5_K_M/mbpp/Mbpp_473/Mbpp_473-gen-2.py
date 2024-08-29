"""
def tuple_intersection(tuples):
    intersection = set(tuples[0])
    for tup in tuples[1:]:
        intersection &= set(tup)
    return intersection
"""

# Tests
assert