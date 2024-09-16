def dict_depth(d):
    if not isinstance(d, dict):
        return 0
    return max(dict_depth(v) for v in d.values()) + 1
