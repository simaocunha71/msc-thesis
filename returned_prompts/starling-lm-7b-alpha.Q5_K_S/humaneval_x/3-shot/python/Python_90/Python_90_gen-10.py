    if len(lst) < 2:
        return None

    m = min(lst)
    idx = lst.index(m)
    lst[idx] = float('inf')
    return min(lst)


