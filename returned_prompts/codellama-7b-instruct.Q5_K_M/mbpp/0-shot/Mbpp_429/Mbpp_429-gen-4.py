def and_tuples(t1, t2):
    return tuple(i & j for i, j in zip(t1, t2))
