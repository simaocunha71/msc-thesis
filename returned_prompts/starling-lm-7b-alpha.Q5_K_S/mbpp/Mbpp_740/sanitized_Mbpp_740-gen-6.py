def tuple_to_dict(t):
    d = {t[0]: t[1]}
    for i in range(2, len(t)):
        d[t[i-1]] = t[i]
    return d