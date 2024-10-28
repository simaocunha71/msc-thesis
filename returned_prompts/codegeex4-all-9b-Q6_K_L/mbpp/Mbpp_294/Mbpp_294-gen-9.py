def max_val(lst):
    max_val = float('-inf')
    for i in lst:
        if isinstance(i, int):
            if i > max_val:
                max_val = i
    return max_val

