def max_val(lst):
    max_value = None
    for i in lst:
        if isinstance(i, int) or isinstance(i, float):
            if max_value is None or i > max_value:
                max_value = i
    return max_value