def filter_data(d, h, w):
    res = {}
    for key, val in d.items():
        if val[0] > h and val[1] > w:
            res[key] = val
    return res