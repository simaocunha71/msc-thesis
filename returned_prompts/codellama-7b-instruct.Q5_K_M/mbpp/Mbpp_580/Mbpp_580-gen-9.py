def extract_even(nested_tuple):
    if type(nested_tuple) == tuple:
        return tuple(filter(lambda x: isinstance(x, int) and x % 2 == 0, nested_tuple))
    else:
        return nested_tuple
