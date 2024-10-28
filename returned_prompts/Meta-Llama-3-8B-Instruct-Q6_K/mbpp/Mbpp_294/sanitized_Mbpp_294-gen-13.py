def max_val(lst):
    max_val = float('-inf')
    for val in lst:
        if isinstance(val, int):
            max_val = max(max_val, val)
    return max_val