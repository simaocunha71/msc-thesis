def extract_even(nested_tuple):
    return tuple(x if isinstance(x, tuple) else x if x % 2 == 0 else extract_even(x) for x in nested_tuple)