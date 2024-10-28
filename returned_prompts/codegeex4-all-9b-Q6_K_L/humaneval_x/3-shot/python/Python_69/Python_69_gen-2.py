    from collections import Counter

    counter = Counter(lst)
    for num, freq in counter.items():
        if freq >= num:
            return num

    return -1

