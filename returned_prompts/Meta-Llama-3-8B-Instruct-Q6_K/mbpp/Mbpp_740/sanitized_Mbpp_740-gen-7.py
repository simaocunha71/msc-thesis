def tuple_to_dict(tup):
    result = {}
    for i in range(0, len(tup), 2):
        result[tup[i]] = tup[i+1]
    return result