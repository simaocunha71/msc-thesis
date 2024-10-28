def dict_depth(dic):
    if isinstance(dic, dict):
        return 1 + max(dict_depth(value) for value in dic.values())
    return 0