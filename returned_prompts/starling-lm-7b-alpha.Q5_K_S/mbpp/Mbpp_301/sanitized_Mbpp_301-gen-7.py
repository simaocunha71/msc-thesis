def dict_depth(d):
    return max(map(dict_depth, d.values())) + 1 if isinstance(d, dict) else 0