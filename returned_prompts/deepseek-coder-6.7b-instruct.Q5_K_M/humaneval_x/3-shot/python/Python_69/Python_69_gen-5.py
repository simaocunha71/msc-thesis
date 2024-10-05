    from collections import Counter
    counter = Counter(lst)

    for i in sorted(counter.keys(), reverse=True):
        if counter[i] >= i:
            return i

    return -1


