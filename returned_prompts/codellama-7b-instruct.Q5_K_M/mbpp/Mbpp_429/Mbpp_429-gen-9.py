def and_tuples(t1, t2):
    return tuple(c1 & c2 for c1, c2 in zip(t1, t2))
