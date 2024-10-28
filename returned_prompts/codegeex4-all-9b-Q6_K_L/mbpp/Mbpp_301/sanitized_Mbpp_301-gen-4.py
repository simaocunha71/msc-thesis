def dict_depth(d):
    depth = 1
    for v in d.values():
        if isinstance(v, dict):
            depth = max(depth, 1 + dict_depth(v))
    return depth