    from collections import Counter
    count = Counter(lst)
    max_val = max(count.keys())
    for i in range(max_val, 0, -1):
        if count[i] >= i:
            return i
    return -1


