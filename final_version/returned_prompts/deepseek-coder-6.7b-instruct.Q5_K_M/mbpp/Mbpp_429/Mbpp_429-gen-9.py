def and_tuples(t1, t2):
    return tuple(map(lambda x, y: x & y, t1, t2))

# Test
print(and_tuples((10, 4, 6, 9), (5, 2, 3, 3)))  # Expected output: (0, 0, 2, 1)

"""
