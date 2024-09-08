def dict_depth(d):
    if d == {}:
        return 0
    else:
        return 1 + max(dict_depth(v) for k, v in d.items() if isinstance(v, dict))