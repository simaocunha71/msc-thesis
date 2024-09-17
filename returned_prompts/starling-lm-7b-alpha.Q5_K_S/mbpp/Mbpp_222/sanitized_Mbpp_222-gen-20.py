def check_type(t):
    t = iter(t)
    return all(type(x) == type(t.next()) for x in t)