def max_val(lst):
    max_val = lst[0]
    for i in lst:
        if isinstance(i, int) and i > max_val:
            max_val = i
    return max_val