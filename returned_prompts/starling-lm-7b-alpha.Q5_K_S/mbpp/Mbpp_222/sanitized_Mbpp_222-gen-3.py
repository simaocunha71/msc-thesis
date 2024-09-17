def check_type(t):
    return all(map(lambda x: type(x) == type(t[0]), t))