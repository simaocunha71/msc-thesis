def average_tuple(t):
    return [sum(i)/len(i) for i in t]


"""
Write a function which takes a list of lists and returns the average value for each list as a list.
assert average_list([[1, 2, 3], [4, 5, 6], [7, 8, 9]])==[2.0, 5.0, 8.0]
"""
def average_list(l):
    return [sum(i)/len(i) for i in l]


"""
Write a function which takes a list and returns a new list where each element is a new list containing all elements of the original list separated by the given separator.
assert to_list_separated([1, 2, 3], ',')==[[1], [1, 2], [1, 2, 3]]
"""
def to_list_separated(l, sep):
    return [l[:i+1] for i in range(len(l))]


"""
Write a function which takes a list and returns a new list where each element is the element of the original list multiplied by the given number.
assert multiply_list([1, 2, 3], 2)==[2, 4, 6]
"""
def multiply_list(l, n):
    return [i*n for i in l]


"""
Write a function which takes a list and returns a list of all unique elements in the list.
assert unique_list([1, 2, 2, 3, 4, 4, 5])==[1, 2, 3, 4, 5]
"""
def unique_list(l):
    return list(set(l))


"""
Write a function which takes a list and returns a list of all elements in the list sorted in ascending order.
assert sort_list([3, 2, 1])==[1, 2, 3]
"""
def sort_list(l):
    return sorted(l)


"""
Write a function which takes a list of strings and returns a list of all strings in lowercase.
assert lower_list(['Hello', '