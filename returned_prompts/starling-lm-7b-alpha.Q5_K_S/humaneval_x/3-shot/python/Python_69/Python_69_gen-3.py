    from collections import Counter
    counter = Counter(lst)
    for num in counter:
        if counter[num] >= num:
            return num
    return -1


