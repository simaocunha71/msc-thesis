    if not lst:
        return None

    lst = sorted(set(lst))
    if len(lst) < 2:
        return None

    return lst[1]  # return the 2nd smallest element


