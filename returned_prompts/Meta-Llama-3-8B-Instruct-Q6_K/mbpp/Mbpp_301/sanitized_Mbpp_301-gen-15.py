def dict_depth(d):
    if not isinstance(d, dict):
        return 0
    depth = 1
    for k, v in d.items():
        depth = max(depth, 1 + dict_depth(v))
    return depth