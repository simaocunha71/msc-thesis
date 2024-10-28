def second_smallest(lst):
    lst = list(set(lst))
    if len(lst) < 2:
        return None
    return sorted(lst)[1]