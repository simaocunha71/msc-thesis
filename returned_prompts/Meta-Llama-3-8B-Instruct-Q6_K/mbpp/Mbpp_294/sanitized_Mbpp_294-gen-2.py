def max_val(lst):
    return max(map(int, [x for x in lst if isinstance(x, int)])) if any(isinstance(x, int) for x in lst) else None