def is_Sub_Array(main_list, sub_list):
    return set(sub_list).issubset(main_list)

print(is_Sub_Array([1,4,3,5],[1,2])) # False

"""
This function works by converting the sub_list and main_list into sets and then checking if the set of the sub_list is a subset of the set of the main_list.
If the sub_list set is a subset of the main_list set, this means that every element in the sub_list is also in the main_list.
"""

