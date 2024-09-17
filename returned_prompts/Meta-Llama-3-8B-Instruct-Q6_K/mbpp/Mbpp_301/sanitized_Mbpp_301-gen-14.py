def dict_depth(d, depth=1):
    if not isinstance(d, dict):
        return depth
    max_depth = depth
    for key, value in d.items():
        max_depth = max(max_depth, dict_depth(value, depth + 1))
    return max_depth