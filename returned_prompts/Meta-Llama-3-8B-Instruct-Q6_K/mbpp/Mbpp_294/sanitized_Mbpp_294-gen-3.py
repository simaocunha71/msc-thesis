def max_val(lst):
    return max(map(int, [i for i in lst if isinstance(i, int)]))
    # return max(i for i in lst if isinstance(i, int))  # Python 3.5+
    # return max(map(int, [i for i in lst if isinstance(i, int)]))  # Python 3.5-