    from collections import Counter

    count = Counter(lst)
    max_freq = max(count.values())
    for num, freq in count.items():
        if num > 0 and freq >= num:
            return num
    return -1


