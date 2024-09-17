def dict_depth(d, depth=1):
    if isinstance(d, dict):
        return max(depth, max(dict_depth(v, depth+1) for v in d.values()))
    return depth

