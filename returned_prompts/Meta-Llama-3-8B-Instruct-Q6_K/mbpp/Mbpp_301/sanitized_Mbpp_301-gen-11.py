def dict_depth(d):
    depth = 1
    for k, v in d.items():
        if isinstance(v, dict):
            depth = max(depth, 1 + dict_depth(v))
    return depth