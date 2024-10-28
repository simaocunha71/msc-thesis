def extract_even(t):
    if isinstance(t, tuple):
        return tuple(filter(lambda x: isinstance(x, tuple) or x%2 == 0, t))
    else:
        return t if t%2 == 0 else None