def check_type(my_tuple):
    if len(my_tuple) == 0:
        return True
    else:
        return isinstance(my_tuple[0], type(my_tuple[1])) and check_type(my_tuple[1:])