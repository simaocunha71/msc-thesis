def recursive_list_sum(my_list):
    if len(my_list) == 0:
        return 0
    elif isinstance(my_list[0], list):
        return recursive_list_sum(my_list[0]) + recursive_list_sum(my_list[1:])
    else:
        return my_list[0] + recursive_list_sum(my_list[1:])