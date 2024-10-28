def extract_even(nested_tuple):
    return tuple(extract_even(x) if isinstance(x, tuple) else x for x in nested_tuple if x % 2 == 0)