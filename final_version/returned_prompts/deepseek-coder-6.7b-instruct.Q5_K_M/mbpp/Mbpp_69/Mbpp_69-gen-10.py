def is_sublist(main_list, sublist):
    return all(item in main_list for item in sublist)

print(is_sublist([2,4,3,5,7],[3,7]))

"""
This function uses the built-in Python function all() to check if all elements in the sublist exist in the main list. If all elements exist in the main list, then the all() function returns True otherwise it returns False.
"""

