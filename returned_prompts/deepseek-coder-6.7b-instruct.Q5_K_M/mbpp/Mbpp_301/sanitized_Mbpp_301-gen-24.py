def dict_depth(d):
    if isinstance(d, dict):
        return 1 + max([dict_depth(v) for v in d.values()] or [0])
    return 0