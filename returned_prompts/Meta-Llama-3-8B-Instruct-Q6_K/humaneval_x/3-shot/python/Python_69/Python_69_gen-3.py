    from collections import Counter

    counter = Counter(lst)
    max_freq = max(counter.values())

    for num, freq in counter.items():
        if freq >= num and num > 0:
            return num

    return -1
