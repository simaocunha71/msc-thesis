def extract_even(t):
    if type(t) is tuple:
        return tuple(filter(lambda x: type(x) in [int, tuple] and x % 2 == 0, t))
    elif type(t) is list:
        return list(filter(lambda x: type(x) in [int, list] and x % 2 == 0, t))
    else:
        return t