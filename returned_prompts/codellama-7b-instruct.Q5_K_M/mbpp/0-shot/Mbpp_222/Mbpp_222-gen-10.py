def check_type(my_tuple):
    return all(isinstance(i, type(my_tuple[0])) for i in my_tuple)


