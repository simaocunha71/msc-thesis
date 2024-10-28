def max_val(lst):
    return max(map(int, [x for x in lst if type(x) == int]))