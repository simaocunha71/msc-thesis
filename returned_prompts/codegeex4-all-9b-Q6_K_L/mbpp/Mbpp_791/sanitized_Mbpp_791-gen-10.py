def remove_nested(tup):
    res = []
    for i in tup:
        if isinstance(i, tuple):
            res.append(remove_nested(i))
        else:
            res.append(i)
    return tuple(res)