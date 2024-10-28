    from collections import Counter
    counter = Counter(lst)
    for i in counter:
        if i > 0 and counter[i] >= i:
            return i
    return -1


