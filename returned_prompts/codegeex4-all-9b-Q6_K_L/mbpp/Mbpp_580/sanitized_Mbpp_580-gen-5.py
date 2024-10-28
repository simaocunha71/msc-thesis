def extract_even(tup):
    """
    This function takes a nested mixed tuple and removes all uneven elements
    """
    res = []
    for el in tup:
        if isinstance(el, tuple):
            res.append(extract_even(el))
        else:
            if el % 2 == 0:
                res.append(el)
    return tuple(res)