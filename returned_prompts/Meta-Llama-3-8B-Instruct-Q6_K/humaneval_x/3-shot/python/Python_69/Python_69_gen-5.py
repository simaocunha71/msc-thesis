    from collections import Counter
    freq = Counter(lst)
    for num in sorted(freq.keys(), reverse=True):
        if num >= freq[num]:
            return num
    return -1
