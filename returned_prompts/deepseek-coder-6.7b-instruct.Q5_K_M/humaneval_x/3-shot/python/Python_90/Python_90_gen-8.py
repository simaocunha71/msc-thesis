    lst = list(set(lst))
    lst.sort()
    if len(lst) < 2:
        return None
    else:
        return lst[1]

