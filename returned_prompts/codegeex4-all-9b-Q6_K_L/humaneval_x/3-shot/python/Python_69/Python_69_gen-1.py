    from collections import Counter
    count = Counter(lst)
    for i in range(max(lst), 0, -1):
        if count[i] >= i:
            return i
    return -1