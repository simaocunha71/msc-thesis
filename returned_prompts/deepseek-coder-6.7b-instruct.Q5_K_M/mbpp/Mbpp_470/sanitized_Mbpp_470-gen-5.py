def add_pairwise(t):
    return tuple(a+b for a, b in zip(t[:-1], t[1:]))