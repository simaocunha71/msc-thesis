def check_type(tup):
    return all(type(i) == type(tup[0]) for i in tup)

