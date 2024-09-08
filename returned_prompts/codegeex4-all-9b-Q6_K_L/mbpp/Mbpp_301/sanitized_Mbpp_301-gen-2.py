def dict_depth(d, level=1):
    if not isinstance(d, dict) or not d:
        return level
    return max(dict_depth(v, level + 1) for v in d.values())