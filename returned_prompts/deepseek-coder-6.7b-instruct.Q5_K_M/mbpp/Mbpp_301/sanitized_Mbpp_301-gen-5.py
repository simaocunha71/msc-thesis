def dict_depth(d):
    if isinstance(d, dict):
        if len(d) == 0:
            return 1
        return 1 + max(dict_depth(v) for v in d.values())
    return 0