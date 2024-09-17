def second_smallest(lst):
    if len(lst) < 2:
        return None
    min_val = min(lst)
    lst = [x for x in lst if x != min_val]
    if len(lst) < 2:
        return None
    return min(lst)