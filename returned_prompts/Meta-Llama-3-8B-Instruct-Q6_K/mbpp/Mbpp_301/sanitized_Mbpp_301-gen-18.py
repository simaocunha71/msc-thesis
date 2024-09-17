def dict_depth(d, depth=1):
    max_depth = depth
    for k, v in d.items():
        if isinstance(v, dict):
            max_depth = max(max_depth, dict_depth(v, depth + 1))
    return max_depth