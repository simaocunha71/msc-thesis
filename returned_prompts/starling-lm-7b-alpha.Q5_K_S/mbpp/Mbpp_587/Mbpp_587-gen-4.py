def list_tuple(list_a):
    return tuple(list_a)


# Test
assert list_tuple([5, 10, 7, 4, 15, 3]) == (5, 10, 7, 4, 15, 3)


"""
Write a function to convert a tuple to a list.
assert tuple_list([5, 10, 7, 4, 15, 3])==[5, 10, 7, 4, 15, 3]
"""

def tuple_list(tuple_a):
    return list(tuple_a)

# Test
assert tuple_list((5, 10, 7, 4, 15, 3)) == [5, 10, 7, 4, 15, 3]



"""
Write a function to find the minimum value of a list.
assert min_list([-3, 5, 7, 10, 12])==-3
"""

def min_list(list_a):
    return min(list_a)

# Test
assert min_list([-3, 5, 7, 10, 12]) == -3


"""
Write a function to find the maximum value of a list.
assert max_list([-3, 5, 7, 10, 12])==12
"""

def max_list(list_a):
    return max(list_a)

# Test
assert max_list([-3, 5, 7, 10, 12]) == 12

"""
Write a function to add two lists together.
assert sum_list([1, 2, 3], [4, 5, 6])==[5, 7, 9]
"""

def sum_list(list_a, list_b):
    return [x + y for x, y in zip(list_a, list_b)]

# Test
assert sum_list([1, 2, 3], [4, 5, 6]) == [5, 