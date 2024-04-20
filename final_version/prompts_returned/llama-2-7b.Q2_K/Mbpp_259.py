"""
Write a function to maximize the given two tuples.
assert maximize_elements(((1, 3), (4, 5), (2, 9), (1, 10)), ((6, 7), (3, 9), (1, 1), (7, 3))) == ((6, 7), (4, 9), (2, 9), (7, 10))
"""

def maximize_elements(tuples):
    """Returns a new tuple consisting of the maximum element from each tuple"""
    for i, tuple in enumerate(tuples):
        if tuples[i][0] > max(tuple[1:], key=lambda x:x[0])[0]:
            return (max(tuple, key=lambda x:x[0])[0],) + tuples[i][1:]
