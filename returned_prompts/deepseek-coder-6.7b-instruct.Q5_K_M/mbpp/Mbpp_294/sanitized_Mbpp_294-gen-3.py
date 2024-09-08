def max_val(lst):
    max_value = None
    for item in lst:
        if max_value is None or (isinstance(item, int) and item > max_value):
            max_value = item
    return max_value