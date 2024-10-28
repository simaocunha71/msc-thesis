def right_insertion(lst, val):
    l, r = 0, len(lst)
    while l < r:
        m = (l + r) // 2
        if lst[m] < val:
            l = m + 1
        else:
            r = m
    return l