def check_type(t):
    t = set(type(i) for i in t)
    return len(t) == 1