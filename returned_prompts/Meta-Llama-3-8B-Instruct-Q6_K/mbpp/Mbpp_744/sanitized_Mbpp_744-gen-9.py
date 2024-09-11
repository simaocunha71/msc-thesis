def check_none(tup):
    return any(item is None for item in tup)  # or return any(item==None for item in tup) for Python 2.7 and below