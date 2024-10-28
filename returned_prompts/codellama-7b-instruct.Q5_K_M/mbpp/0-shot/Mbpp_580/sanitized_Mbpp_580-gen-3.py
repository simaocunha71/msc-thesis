def extract_even(nested_tuple):
    return tuple(map(lambda x: x if isinstance(x, tuple) else x, nested_tuple))