def filter_data(d, h_min, w_min):
    res = {}
    for k, v in d.items():
        if v[0] > h_min and v[1] > w_min:
            res[k] = v
    return res