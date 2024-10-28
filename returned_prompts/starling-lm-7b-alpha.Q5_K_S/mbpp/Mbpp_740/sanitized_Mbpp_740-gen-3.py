def tuple_to_dict(t):
    d = {}
    for i in range(0, len(t) - 1, 2):
        d[t[i]] = t[i + 1]
    return d