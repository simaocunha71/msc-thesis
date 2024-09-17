def tuple_to_dict(t):
    if len(t) % 2 != 0:
        raise ValueError("Tuple must have an even number of elements")
    result = {}
    for i in range(0, len(t), 2):
        result[t[i]] = t[i+1]
    return result