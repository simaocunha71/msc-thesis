"""
def recursive_list_sum(my_list):
    if not my_list:
        return 0
    if isinstance(my_list[0], list):
        return recursive_list_sum(my_list[0]) + recursive_list_sum(my_list[1:])
    else:
        return my_list[0] + recursive_list_sum(my_list[1:])
"""
