    from collections import Counter
    c = Counter(lst)
    max_val = max(c.keys())
    for i in range(max_val, 0, -1):
        if i in c and c[i] >= i:
            return i
    return -1


