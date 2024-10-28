def remove_nested(tup):
    new_tup = []
    for i in tup:
        if type(i) != tuple:
            new_tup.append(i)
    return tuple(new_tup)