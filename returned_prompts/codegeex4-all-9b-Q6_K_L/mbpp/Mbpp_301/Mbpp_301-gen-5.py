def dict_depth(d: dict, depth=1):
    if isinstance(d, dict):
        return max(dict_depth(v, depth+1) for v in d.values()) if d else depth
    return depth

