    if len(lst) < 2:
        return None

    lst.sort()
    if lst[0] == lst[1]:
        return None
    return lst[1]




