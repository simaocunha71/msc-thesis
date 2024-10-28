def min_val(lst):
    min_val = None
    for i in lst:
        if type(i) == int or type(i) == float:
            if min_val is None or i < min_val:
                min_val = i
    return min_val

