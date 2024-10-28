def flatten_list(my_list):
    res = []
    for i in my_list:
        if isinstance(i, list):
            res.extend(flatten_list(i))
        else:
            res.append(i)
    return res