def last(lst, num):
    idx = len(lst) - 1
    while idx >= 0:
        if lst[idx] == num:
            return idx
        idx -= 1
    return -1