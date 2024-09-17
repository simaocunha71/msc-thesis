
def dict_depth(d):
    max_depth = 1
    for v in d.values():
        if isinstance(v, dict):
            max_depth = max(max_depth, dict_depth(v)+1)
    return max_depth


