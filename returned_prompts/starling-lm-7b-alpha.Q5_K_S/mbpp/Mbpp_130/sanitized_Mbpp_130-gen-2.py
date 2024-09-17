def max_occurrences(lst):
    d = {}
    for i in lst:
        if i in d:
            d[i] += 1
        else:
            d[i] = 1
    max_count = 0
    max_item = None
    for i in d:
        if d[i] > max_count:
            max_count = d[i]
            max_item = i
    return max_item