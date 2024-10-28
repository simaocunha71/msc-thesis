def extract_even(t):
    if isinstance(t, tuple):
        return tuple(extract_even(e) if isinstance(e, tuple) else e for e in t if isinstance(e, int) and e % 2 == 0)
    else:
        return t