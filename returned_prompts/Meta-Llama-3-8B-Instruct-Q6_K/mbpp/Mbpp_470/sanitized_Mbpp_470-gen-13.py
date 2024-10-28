def add_pairwise(t):
    if len(t) < 2:
        if len(t) == 0:
            return ()
        return t
    return tuple(a + b for a, b in zip(t, t[1:]))