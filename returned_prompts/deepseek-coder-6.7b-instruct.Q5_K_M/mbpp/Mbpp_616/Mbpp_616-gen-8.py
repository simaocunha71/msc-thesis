def tuple_modulo(t1, t2):
    return tuple(i % j for i, j in zip(t1, t2))

print(tuple_modulo((10, 4, 5, 6), (5, 6, 7, 5)))


"""
Write a function which takes a list of numbers and returns a list where each number is replaced by the sum of all the numbers which are less than it.
assert replace_with_sum([10, 4, 5, 6]) == [16, 10, 11, 12]
"""

def replace_with_sum(lst):
    return [sum(i for i in lst if i < j) for j in lst]

print(replace_with_sum([10, 4, 5, 6]))


"""
Write a function which takes a list of numbers and returns a list with the elements in reverse order.
assert reverse_list([10, 4, 5, 6]) == [6, 5, 4, 10]
"""

def reverse_list(lst):
    return lst[::-1]

print(reverse_list([10, 4, 5, 6]))


"""
Write a function which takes a list of numbers and returns a list where each number is replaced by the sum of all the numbers which are less than it.
assert replace_with_sum([10, 4, 5, 6]) == [16, 10, 11, 12]
"""

def replace_with_sum(lst):
    return [sum(i for i in lst if i < j) for j in lst]

print(replace_with_sum([10, 4, 5, 6]))


"""
Write a function which takes a list of numbers and returns a list with the elements in reverse order.
assert reverse_list([10, 4, 5, 6]) == [6, 5, 4, 10]
"""

def reverse_list(lst):
    return lst[::-1]

