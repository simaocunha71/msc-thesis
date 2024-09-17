def max_val(lst):
    if isinstance(lst[0], int):
        return max(lst)
    else:
        return max(map(max_val, lst))