def max_val(lst):
    return max(map(int, [i for i in lst if isinstance(i, int)]))