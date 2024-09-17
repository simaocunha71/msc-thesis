def dict_depth(d):
    max_depth = 0
    for k, v in d.items():
        if isinstance(v, dict):
            depth = dict_depth(v) + 1
            max_depth = max(max_depth, depth)
    return max_depth