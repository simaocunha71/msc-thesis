def extract_even(tup):
    return tuple(i if isinstance(i, tuple) else i if i % 2 == 0 else None for i in tup if isinstance(i, tuple) or i % 2 == 0)