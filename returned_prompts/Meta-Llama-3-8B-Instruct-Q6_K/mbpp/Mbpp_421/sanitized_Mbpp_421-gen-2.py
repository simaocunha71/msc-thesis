def concatenate_tuple(tup):
    return '-'.join(map(str, tup)) if isinstance(tup, tuple) else 'Invalid input'