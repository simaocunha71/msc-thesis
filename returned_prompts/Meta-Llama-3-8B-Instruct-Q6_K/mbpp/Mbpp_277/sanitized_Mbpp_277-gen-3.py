def dict_filter(d, n):
    return {k: v for k, v in d.items() if v >= n}  # use dictionary comprehension to filter the dictionary