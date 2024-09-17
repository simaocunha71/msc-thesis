def remove_nested(test_tup):
    return tuple(filter(lambda x: not isinstance(x, tuple), test_tup))