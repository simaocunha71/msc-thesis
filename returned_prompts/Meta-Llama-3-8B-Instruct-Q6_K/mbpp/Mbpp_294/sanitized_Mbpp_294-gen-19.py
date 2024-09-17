def max_val(lst):
    max_val = float('-inf')
    for val in lst:
        if isinstance(val, int) and val > max_val:
            max_val = val
    return max_val