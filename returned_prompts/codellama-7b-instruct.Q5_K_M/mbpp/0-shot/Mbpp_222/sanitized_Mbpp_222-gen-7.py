def check_type(my_tuple):
    data_type = type(my_tuple[0])
    for i in range(1, len(my_tuple)):
        if type(my_tuple[i]) != data_type:
            return False
    return True