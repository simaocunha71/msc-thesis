def tuple_modulo(t1, t2):
    return tuple(i % j for i, j in zip(t1, t2))

# assert tuple_modulo((10, 4, 5, 6), (5, 6, 7, 5)) == (0, 4, 5, 1)
# print(tuple_modulo((10, 4, 5, 6), (5, 6, 7, 5)))


"""
Write a function which takes two lists of the same length and performs the element wise modulo.
assert list_modulo([10, 4, 5, 6], [5, 6, 7, 5]) == [0, 4, 5, 1]
"""

def list_modulo(l1, l2):
    return [i % j for i, j in zip(l1, l2)]

# assert list_modulo([10, 4, 5, 6], [5, 6, 7, 5]) == [0, 4, 5, 1]
# print(list_modulo([10, 4, 5, 6], [5, 6, 7, 5]))

"""
Write a function which takes two lists of the same length and performs element wise addition.
assert add_lists([10, 4, 5, 6], [5, 6, 7, 5]) == [15, 10, 12, 11]
"""

def add_lists(l1, l2):
    return [i + j for i, j in zip(l1, l2)]

# assert add_lists([10, 4, 5, 6], [5, 6, 7, 5]) == [15, 10, 12, 11]
# print(add_lists([10, 4, 5, 6], [5, 6, 7, 5]))

"""
Write a function which takes two lists of the same length and performs element wise subtraction.
assert subtract_lists([10,