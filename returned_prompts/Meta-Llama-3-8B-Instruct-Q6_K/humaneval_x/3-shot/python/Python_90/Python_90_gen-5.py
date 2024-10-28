    lst = sorted(set(lst))  # remove duplicates and sort the list
    if len(lst) < 2:
        return None
    return lst[1]  # return the 2nd smallest element


