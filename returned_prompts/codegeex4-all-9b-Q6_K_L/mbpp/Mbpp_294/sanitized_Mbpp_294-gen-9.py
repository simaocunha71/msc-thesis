def max_val(lst):
    max_val = None
    for i in lst:
        if isinstance(i, int) and (max_val is None or i > max_val):
            max_val = i
    return max_val