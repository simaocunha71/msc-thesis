    from collections import Counter

    counter = Counter(lst)
    for k, v in counter.items():
        if k >= v:
            return k
    return -1

