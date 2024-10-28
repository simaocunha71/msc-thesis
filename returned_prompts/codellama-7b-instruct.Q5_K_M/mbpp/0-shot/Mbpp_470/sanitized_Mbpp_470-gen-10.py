def add_pairwise(t):
    return tuple(i + j for i, j in zip(t, t[1:]))