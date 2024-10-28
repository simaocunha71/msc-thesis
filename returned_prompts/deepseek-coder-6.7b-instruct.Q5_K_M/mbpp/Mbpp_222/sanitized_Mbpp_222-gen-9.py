def check_type(tup):
    first_type = type(tup[0])
    return all(type(x) == first_type for x in tup)