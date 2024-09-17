def extract_even(t):
    if isinstance(t, tuple):
        return (x for x in t if not isinstance(x, tuple) or extract_even(x) and x % 2 == 0)
    else:
        return t % 2 == 0