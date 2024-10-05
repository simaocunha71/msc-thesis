    for i in sorted(lst, reverse=True):
        if lst.count(i) >= i:
            return i
    return -1


