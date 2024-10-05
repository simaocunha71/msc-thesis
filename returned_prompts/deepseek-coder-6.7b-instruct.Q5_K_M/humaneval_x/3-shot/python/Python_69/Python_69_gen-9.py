    from collections import Counter
    count = Counter(lst)
    for i in sorted(count.keys(), reverse=True):
        if count[i] >= i:
            return i
    return -1


