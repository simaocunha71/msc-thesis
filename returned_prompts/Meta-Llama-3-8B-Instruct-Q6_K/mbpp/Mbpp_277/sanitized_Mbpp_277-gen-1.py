def dict_filter(d, n):
    return {k: v for k, v in d.items() if v >= n}  # filter dictionary items by value