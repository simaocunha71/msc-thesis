
def is_sublist(main_list, sub_list):
    return sub_list in main_list

print(is_sublist([2,4,3,5,7],[3,7])) # returns False
"""
The function is_sublist checks if the sublist is in the main list. Python's "in" operator is used for this purpose. If the sublist is found in the main list, it returns True, else it returns False.
"""

