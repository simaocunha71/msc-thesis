
def max_val(lst):
    return max(lst, key=lambda x: (isinstance(x, int), x))


