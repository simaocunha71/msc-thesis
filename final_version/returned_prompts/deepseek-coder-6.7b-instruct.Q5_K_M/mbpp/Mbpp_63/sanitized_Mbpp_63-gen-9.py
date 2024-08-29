def max_difference(lst):
    return max(max(x)-min(x) for x in lst)