def remove_nested(tup):
    if type(tup) == tuple:
        return sum(map(remove_nested, tup), ())
    else:
        return tup