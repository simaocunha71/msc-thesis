def recursive_list_sum(my_list):
    if not isinstance(my_list, list):
        return my_list
    else:
        return sum(map(recursive_list_sum, my_list))