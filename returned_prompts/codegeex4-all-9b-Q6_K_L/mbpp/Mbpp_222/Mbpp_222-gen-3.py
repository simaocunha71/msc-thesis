def check_type(tup):
    return all(type(x) == type(tup[0]) for x in tup)