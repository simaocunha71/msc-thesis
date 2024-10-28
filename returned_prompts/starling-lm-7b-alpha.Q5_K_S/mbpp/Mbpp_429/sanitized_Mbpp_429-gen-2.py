def and_tuples(t1, t2):
    return tuple(t1[i] & t2[i] for i in range(len(t1)))