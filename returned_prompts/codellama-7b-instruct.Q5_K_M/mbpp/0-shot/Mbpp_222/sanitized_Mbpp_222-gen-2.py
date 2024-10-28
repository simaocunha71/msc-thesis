def check_type(my_tuple):
    if len(my_tuple) == 0:
        return True
    else:
        return all(isinstance(i, type(my_tuple[0])) for i in my_tuple)