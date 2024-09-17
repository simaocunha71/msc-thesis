
def dict_depth(d):
    max_depth = 0
    for k, v in d.items():
        if isinstance(v, dict):
            max_depth = max(max_depth, dict_depth(v) + 1)
    return max_depth + 1


