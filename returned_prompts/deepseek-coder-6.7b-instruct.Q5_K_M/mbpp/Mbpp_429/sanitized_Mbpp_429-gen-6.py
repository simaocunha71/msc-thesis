def and_tuples(t1, t2):
    if len(t1) != len(t2):
        return "Tuples are not of the same length"
    return tuple(i & j for i, j in zip(t1, t2))