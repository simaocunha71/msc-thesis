def check_type(tup):
    return all(map(lambda x: type(x) == tup[0][0], tup))