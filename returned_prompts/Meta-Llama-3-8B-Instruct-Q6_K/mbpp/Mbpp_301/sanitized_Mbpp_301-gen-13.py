def dict_depth(d, depth=1):
    if not d:
        return depth
    max_depth = depth
    for k, v in d.items():
        if isinstance(v, dict):
            max_depth = max(max_depth, dict_depth(v, depth+1))
        else:
            max_depth = max(max_depth, depth)
    return max_depth