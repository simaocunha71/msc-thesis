def dict_depth(d):
    res = 0
    for k, v in d.items():
        if isinstance(v, dict):
            res = max(res, dict_depth(v)+1)
    return res