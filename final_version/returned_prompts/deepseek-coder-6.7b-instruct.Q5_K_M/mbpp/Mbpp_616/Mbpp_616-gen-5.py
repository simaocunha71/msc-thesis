def tuple_modulo(t1, t2):
    return tuple(map(lambda x, y: x % y, t1, t2))

print(tuple_modulo((10, 4, 5, 6), (5, 6, 7, 5)))

"""
Output:
(0, 4, 5, 1)
"""

# Test Case 2
