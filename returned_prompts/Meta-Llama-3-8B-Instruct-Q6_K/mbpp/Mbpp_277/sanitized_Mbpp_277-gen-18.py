def dict_filter(d, n):
    if not d:
        return None
    d.clear()
    for k, v in d.items():
        if v >= n:
            d[k] = v