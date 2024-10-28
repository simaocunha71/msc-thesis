def min_val(lst):
    return min(i for i in lst if isinstance(i, (int, float)))  # or use min(map(int, [x for x in lst if isinstance(x, int)])) for a more explicit version