    from collections import Counter

    lst = [x for x in lst if x > 0]
    counter = Counter(lst)

    for num in sorted(counter, reverse=True):
        if counter[num] >= num:
            return num

    return -1


