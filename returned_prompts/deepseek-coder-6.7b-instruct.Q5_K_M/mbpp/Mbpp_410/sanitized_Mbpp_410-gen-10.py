def min_val(lst):
    min_num = None
    for item in lst:
        if isinstance(item, int):
            if min_num is None or item < min_num:
                min_num = item
    return min_num