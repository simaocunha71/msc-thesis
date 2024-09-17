def dict_depth(d):
    if isinstance(d, dict):
        if not d:
            return 1
        return 1 + max(dict_depth(v) for v in d.values())
    return 0