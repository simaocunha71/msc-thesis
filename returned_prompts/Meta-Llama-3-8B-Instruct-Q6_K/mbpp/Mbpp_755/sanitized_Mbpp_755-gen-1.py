def second_smallest(lst):
    if len(lst) < 2:
        return None
    lst = sorted(set(lst))
    if len(lst) < 2:
        return None
    return lst[1]  # return second smallest number