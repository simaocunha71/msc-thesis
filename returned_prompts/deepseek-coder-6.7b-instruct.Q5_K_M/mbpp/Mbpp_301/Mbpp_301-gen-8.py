
def dict_depth(d):
    if isinstance(d, dict):
        if d:
            return 1 + max(dict_depth(d[k]) for k in d)
        return 0
    return 0


