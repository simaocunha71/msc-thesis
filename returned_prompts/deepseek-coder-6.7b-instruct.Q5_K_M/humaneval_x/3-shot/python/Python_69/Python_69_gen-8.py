    from collections import Counter
    c = Counter(lst)
    max_val = max(c.keys())
    for key in sorted(c.keys(), reverse=True):
        if c[key] >= key:
            return key
    return -1


