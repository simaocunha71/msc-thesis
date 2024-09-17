
def check_type(my_tuple):
    if len(my_tuple) == 0:
        return True
    else:
        return all(isinstance(x, type(my_tuple[0])) for x in my_tuple)


