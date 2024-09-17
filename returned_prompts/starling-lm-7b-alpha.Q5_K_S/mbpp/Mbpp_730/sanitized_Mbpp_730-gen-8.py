def consecutive_duplicates(list):
    prev = None
    res = []
    for x in list:
        if prev is None or x != prev:
            res.append(x)
        prev = x
    return res