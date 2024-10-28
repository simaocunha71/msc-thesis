    for i in range(1, len(lst)):
        if lst.count(i) >= i:
            return i
    return -1


