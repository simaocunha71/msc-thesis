def flatten_list(nested_list):
    res = []
    for item in nested_list:
        if isinstance(item, list):
            res.extend(flatten_list(item))
        else:
            res.append(item)
    return res
