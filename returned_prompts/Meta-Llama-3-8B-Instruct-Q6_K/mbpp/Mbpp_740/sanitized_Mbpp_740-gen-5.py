def tuple_to_dict(tup):
    dict = {}
    for i in range(0, len(tup), 2):
        dict[tup[i]] = tup[i+1]
    return dict