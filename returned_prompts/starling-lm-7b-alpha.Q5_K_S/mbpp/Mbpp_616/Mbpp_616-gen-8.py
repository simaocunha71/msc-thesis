def tuple_modulo(t1, t2):
    return tuple(i % j for i, j in zip(t1, t2))


# Testing
assert tuple_modulo((10, 4, 5, 6), (5, 6, 7, 5)) == (0, 4, 5, 1)


# Further testing
assert tuple_modulo((12, 4, 5, 6), (5, 6, 7, 5)) == (2, 4, 5, 1)
assert tuple_modulo((15, 4, 5, 6), (5, 6, 7, 5)) == (0, 4, 5, 1)

# More testing
assert tuple_modulo((13, 4, 5, 6), (5, 6, 7, 5)) == (3, 4, 5, 1)






def tuple_modulo(t1, t2):
    return tuple(i % j for i, j in zip(t1, t2))

# Testing
assert tuple_modulo((10, 4, 5, 6), (5, 6, 7, 5)) == (0, 4, 5, 1)

# Further testing
assert tuple_modulo((12, 4, 5, 6), (5, 6, 7, 5)) == (2, 4, 5, 1)
assert tuple_modulo((15, 4, 5, 6), (5, 6, 7, 5)) == (0, 4, 5, 1)

# More testing
assert tuple_modulo((13, 4, 5, 6), (5, 6, 7, 5)) == (3, 4, 5, 1)


# More testing
assert tuple_modulo((10, 4, 5, 6), (5, 6, 7, 5)) == (0, 4, 5, 1)
assert tuple_mod