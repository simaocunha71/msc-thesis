def dict_depth(d):
    return 1 + max(dict_depth(v) for v in d.values()) if d else 0