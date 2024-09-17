
def remove_nested(input_tuple):
    return tuple(i for i in input_tuple if not isinstance(i, tuple))


