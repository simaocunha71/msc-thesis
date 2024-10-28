def remove_nested(t):
    new_t = ()
    for i in t:
        if isinstance(i, tuple):
            for j in i:
                new_t = new_t + (j,)
        else:
            new_t = new_t + (i,)
    return new_t