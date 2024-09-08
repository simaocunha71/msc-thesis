def extract_even(mixed_tuple):
    return tuple(filter(lambda x: isinstance(x, tuple) or x % 2 == 0, mixed_tuple))