def count_first_elements(tup):
    if isinstance(tup, tuple):
        return sum(1 for i in tup if not isinstance(i, tuple))
    else:
        return 0