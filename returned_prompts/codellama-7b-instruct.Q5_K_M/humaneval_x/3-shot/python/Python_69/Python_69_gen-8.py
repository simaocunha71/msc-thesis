    if len(lst) == 0:
        return -1

    freq_map = {}
    for i in lst:
        if i in freq_map:
            freq_map[i] += 1
        else:
            freq_map[i] = 1

    for i in range(1, len(lst)):
        if freq_map[i] >= i and i >= 1:
            return i
    return -1


