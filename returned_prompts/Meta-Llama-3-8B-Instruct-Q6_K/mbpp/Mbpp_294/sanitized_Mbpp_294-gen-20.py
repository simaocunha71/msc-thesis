def max_val(lst):
    integers = [x for x in lst if isinstance(x, int)]
    if not integers:
        return None
    return max(integers)