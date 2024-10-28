def dict_depth(d):
    return max([len(d.keys())]+[dict_depth(v) for v in d.values()])