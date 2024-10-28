def flatten_list(my_list):
    if not my_list:
        return my_list
    if isinstance(my_list[0], list):
        return flatten_list(my_list[0]) + flatten_list(my_list[1:])
    return [my_list[0]] + flatten_list(my_list[1:])