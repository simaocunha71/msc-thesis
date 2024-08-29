def is_sublist(main_list, sublist):
    return sublist in main_list

print(is_sublist([2,4,3,5,7],[2,4,3,5,7,9])) # False

"""
Write a function to check whether a list contains the given sublist or not.
assert is_sublist([2,4,3