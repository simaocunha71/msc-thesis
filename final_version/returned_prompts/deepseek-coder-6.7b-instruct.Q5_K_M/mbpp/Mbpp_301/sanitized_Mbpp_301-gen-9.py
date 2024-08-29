def dict_depth(d):
    if not isinstance(d, dict):
        return 0
    if not d:
        return 1
    depths = [dict_depth(v) for v in d.values()]
    return max(depths) + 1