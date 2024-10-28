def add_pairwise(t):
    return tuple(a+b for a,b in zip(t, t[1:]))