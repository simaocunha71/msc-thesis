def filter_data(d, h, w):
    res = {}
    for key, val in d.items():
        if val[0] > h and val[1] > w:
            res[key] = val
    return res


# Another Solution
def filter_data(d, h, w):
    return {k: v for k, v in d.items() if v[0] > h and v[1] > w}


# Another Solution
def filter_data(d, h, w):
    return {k: v for k, v in d.items() if (v[0] > h) and (v[1] > w)}


# Another Solution
def filter_data(d, h, w):
    return {k: v for k, v in d.items() if v[0] > h and v[1] > w}


# Another Solution
def filter_data(d, h, w):
    res = {}
    for k, v in d.items():
        if v[0] > h and v[1] > w:
            res[k] = v
    return res


# Another Solution
def filter_data(d, h, w):
    return {k: v for k, v in d.items() if v[0] > h and v[1] > w}


# Another Solution
def filter_data(d, h, w):
    res = {}
    for k, v in d.items():
        if v[0] > h and v[1] > w:
            res[k] = v
    return res


# Another Solution
def filter_data(d, h, w):
    return {k: v for (k, v) in d.items() if (v[0] > h) and (v[1] > w)}


# Another Solution
def filter_data(d, h, w):
    res = {}
    for k, v in d.items():
        if v[0] > h and v[1] > w:
            res[k] = v
    return res


# Another Solution
def filter_data(d,