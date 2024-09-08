
def swap_List(lst):
    lst[0], lst[-1] = lst[-1], lst[0]
    return lst

print(swap_List([12, 35, 9, 56, 24]))

"""
The function swap_List accepts a list as input. It then uses Python's in-built list indexing feature to interchange the first and last elements of the list. It returns the modified list.
"""

"""
The function swap_List works by swapping the first and last elements of the list. Python's list indexing feature is used to get the first and last elements of the list. The syntax lst[0] gets the first element and lst[-1] gets the last element of the list. The syntax lst[0], lst[-1] = lst[-1], lst[0] is used to swap these two elements.
"""

"""
The function swap_List returns the modified list after the swap operation.
"""

"""
The function swap_List modifies the original list. If you want to keep the original list unchanged, you can create a copy of the list before the swap operation.
"""

"""
The function swap_List assumes that the input list is non-empty. If the list can be empty, you should add a check for this case.
"""

"""
The function swap_List works with any type of elements in the list, not just numbers. For example, it can work with strings, tuples, etc.
"""

"""
The function swap_List has a time complexity of O(1), which means it takes a constant amount of time to execute regardless of the size of the input list. This is because it only performs a single operation (the swap) regardless of the size of the list.
"""

"""
The function swap_List has a space complexity of O(1), which means it uses a constant amount of space. This is because it only needs a single extra variable to perform the swap operation.
"""
<jupyter_output>
<empty_output>
<jupyter_text>
