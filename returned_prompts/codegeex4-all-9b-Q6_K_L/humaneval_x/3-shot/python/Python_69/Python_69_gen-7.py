    from collections import Counter

    counter = Counter(lst)

    for key, value in counter.items():
        if key < value:
            return key

    return -1

