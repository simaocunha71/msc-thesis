def is_Sub_Array(main_list, sub_list):
    return sub_list in main_list

print(is_Sub_Array([1,4,3,5],[1,2])) # False

"""
This function works by using the 'in' operator in Python which checks for the presence of an element in a list.
So, it returns True if the sub_list is present in main_list else it returns False.
"""

