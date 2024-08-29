def remove_nested(tup):
    res = []
    for i in tup:
        if type(i) != tuple:
            res.append(i)
    return tuple(res)

assert remove_nested((1, 5, 7, (4, 6), 10)) == (1, 5, 7, 10)


