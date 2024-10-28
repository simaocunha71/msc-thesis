def check_type(tup):
    return all(type(tup[0]) == type(i) for i in tup)