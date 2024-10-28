def min_val(lst):
    min_value = None
    for item in lst:
        if isinstance(item, int):
            if min_value is None or item < min_value:
                min_value = item
    return min_value

