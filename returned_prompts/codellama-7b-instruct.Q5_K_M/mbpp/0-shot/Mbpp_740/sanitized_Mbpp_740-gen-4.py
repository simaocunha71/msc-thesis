def tuple_to_dict(tup):
    dct = {}
    for i in range(0, len(tup), 2):
        dct[tup[i]] = tup[i+1]
    return dct