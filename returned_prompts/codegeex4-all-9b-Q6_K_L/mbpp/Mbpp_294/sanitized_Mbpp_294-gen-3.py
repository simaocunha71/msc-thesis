def max_val(lst):
    max_val = None
    for item in lst:
        if isinstance(item, int):
            if max_val is None or item > max_val:
                max_val = item
    return max_val