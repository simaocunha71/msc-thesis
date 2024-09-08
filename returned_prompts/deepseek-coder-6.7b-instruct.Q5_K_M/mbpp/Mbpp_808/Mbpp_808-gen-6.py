
def check_K(tuples, k):
    return k in tuples

print(check_K((10, 4, 5, 6, 8), 6))  # True

# 2.
"""
Write a Python program to get the 4th element from the first and the 4th element from the last of the tuple.
"""

def get_fourth(tuples):
    return tuples[3], tuples[-4]

print(get_fourth((10, 4, 5, 6, 8, 12, 14, 18)))  # (6, 12)

# 3.
"""
Write a Python program to swap the first and last element of the list.
"""

def swap_first_last(lst):
    lst[0], lst[-1] = lst[-1], lst[0]
    return lst

print(swap_first_last([10, 4, 5, 6, 8]))  # [8, 4, 5, 6, 10]

# 4.
"""
Write a Python program to remove the nth index element from the list.
"""

def remove_nth(lst, n):
    del lst[n]
    return lst

print(remove_nth([10, 4, 5, 6, 8], 2))  # [10, 4, 6, 8]

# 5.
"""
Write a Python program to slice a tuple.
"""

def slice_tuple(tuples, start, end):
    return tuples[start:end]

print(slice_tuple((10, 4, 5, 6, 8, 12, 14, 18), 2, 5))  # (5, 6, 8)

# 6.
"""
Write a Python program to reverse a tuple.
"""

def reverse_tuple(tuples):
    return tuples[::-1]

print(reverse_