def remove_nested(tup):
    res = []
    for i in tup:
        if type(i) != tuple:
            res.append(i)
    return tuple(res)