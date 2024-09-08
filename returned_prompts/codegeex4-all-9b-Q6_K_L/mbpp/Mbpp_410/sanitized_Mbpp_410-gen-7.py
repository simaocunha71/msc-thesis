def min_val(lst):
    min_val = float('inf')
    for item in lst:
        if isinstance(item, int) and item < min_val:
            min_val = item
    return min_val