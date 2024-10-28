    if len(lst) == 0:
        return -1
    if len(lst) == 1:
        return lst[0]

    max_val = max(lst)
    if lst.count(max_val) >= max_val:
        return max_val

    for i in range(max_val - 1, 0, -1):
        if lst.count(i) >= i:
            return i
    return -1


