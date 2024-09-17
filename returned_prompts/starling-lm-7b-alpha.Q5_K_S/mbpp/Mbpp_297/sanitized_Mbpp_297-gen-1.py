def flatten_list(lst):
    res = []
    for i in lst:
        if isinstance(i, list):
            res.extend(flatten_list(i))
        else:
            res.append(i)
    return res