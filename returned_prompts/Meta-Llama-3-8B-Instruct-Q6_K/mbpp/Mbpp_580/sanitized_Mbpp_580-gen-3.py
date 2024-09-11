def extract_even(tup):
    return tuple(x if isinstance(x, tuple) else (x if x % 2 == 0 else None) for x in tup) if None not in tup else None