    lst = sorted(lst)
    if len(lst) < 2:
        return None
    return lst[1] if lst[0] == lst[1] else lst[1] if len(lst) > 2 else None


