    from collections import Counter
    m = Counter(lst)
    for i in lst:
        if i > 0 and m[i] >= i:
            return i
    return -1


