def recursive_list_sum(my_list):
    if isinstance(my_list[0], list):
        return sum(recursive_list_sum(my_list[0]))
    else:
        return sum(my_list)