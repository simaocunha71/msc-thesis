    from collections import Counter
    counter = Counter(lst)
    max_value = max(counter.keys())
    for i in range(max_value, 0, -1):
        if counter[i] >= i:
            return i
    return -1


