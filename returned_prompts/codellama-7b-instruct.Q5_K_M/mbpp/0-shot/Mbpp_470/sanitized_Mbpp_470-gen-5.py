def add_pairwise(t):
    return tuple(b + a for a, b in zip(t, t[1:]))