def remove_nested(tup):
    new_tup = ()
    for i in tup:
        if isinstance(i, tuple):
            new_tup += i
        else:
            new_tup += (i,)
    return new_tup