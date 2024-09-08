def and_tuples(t1, t2):
    return tuple(i & j for i, j in zip(t1, t2))

assert and_tuples((10, 4, 6, 9), (5, 2, 3, 3)) == (0, 0, 2, 1)
"""

