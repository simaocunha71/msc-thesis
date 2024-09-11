def dict_depth(d, depth=1):
    if not isinstance(d, dict) or not d:
        return depth
    return max(dict_depth(v, depth+1) for v in d.values())