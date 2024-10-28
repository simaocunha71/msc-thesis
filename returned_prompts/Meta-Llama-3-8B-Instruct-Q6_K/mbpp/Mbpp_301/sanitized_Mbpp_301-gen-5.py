def dict_depth(d, depth=0):
    if not isinstance(d, dict):
        return depth
    return max(dict_depth(v, depth + 1) for v in d.values()) if d else depth