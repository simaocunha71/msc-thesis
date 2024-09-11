def concatenate_tuple(t):
    return '-'.join(str(x) for x in t) if isinstance(t, tuple) else 'Invalid input'