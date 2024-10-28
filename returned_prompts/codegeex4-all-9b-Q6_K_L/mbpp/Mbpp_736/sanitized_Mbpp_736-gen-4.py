def left_insertion(lst, x):
    l, r = 0, len(lst)
    while l < r:
        m = (l + r) // 2
        if lst[m] < x:
            l = m + 1
        else:
            r = m
    return l