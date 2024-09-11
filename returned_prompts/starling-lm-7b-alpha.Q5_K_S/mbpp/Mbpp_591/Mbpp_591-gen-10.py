def swap_List(a):
    # swap the first and last element of the list
    a[0], a[-1] = a[-1], a[0]
    return a

# test the function
assert swap_List([12, 35, 9, 56, 24]) == [24, 35, 9, 56, 12]





def swap_List(a):
    # swap the first and last element of the list
    a[0], a[-1] = a[-1], a[0]
    return a

# test the function
assert swap_List([12, 35, 9, 56, 24]) == [24, 35, 9, 56, 12]


"""
To swap two elements of a list, you can use tuple packing and unpacking in Python. This approach is more Pythonic and efficient. In the tuple packing, the first element of the list is assigned to the last element and vice versa.
"""


def swap_List(a):
    # swap the first and last element of the list
    a[0], a[-1] = a[-1], a[0]
    return a

# test the function
assert swap_List([12, 35, 9, 56, 24]) == [24, 35, 9, 56, 12]


"""
To swap two elements in a list, you can use the Python built-in function `list.reverse()` along with slicing to get the first and last elements of the list. Then you can use tuple packing and unpacking to swap these two elements.
"""

def swap_List(a):
    # swap the first and last element of the list
    a[0], a[-1] = a[-1], a[0]
    return a

# test the function
assert swap_List([12, 35, 9, 56, 24]) == [24, 35, 9, 56, 12]



"""
To swap two elements in a list,