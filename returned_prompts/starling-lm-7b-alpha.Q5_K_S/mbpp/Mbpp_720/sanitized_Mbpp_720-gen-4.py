def add_dict_to_tuple(tup,dic):
    res = []
    res.extend(list(tup))
    res.extend(list(dic.values()))
    res.extend(list(dic.keys()))
    return tuple(res)