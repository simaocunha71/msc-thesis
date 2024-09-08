def max_val(lst):
    max_val = -float('inf')
    for item in lst:
        if isinstance(item, int) or isinstance(item, float):
            max_val = max(max_val, item)
    return max_val