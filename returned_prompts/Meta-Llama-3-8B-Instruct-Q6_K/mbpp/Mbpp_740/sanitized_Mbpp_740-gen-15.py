def tuple_to_dict(t):
    result = {}
    for i in range(0, len(t), 2):
        if i + 1 < len(t):
            result[t[i]] = t[i + 1]
    return result