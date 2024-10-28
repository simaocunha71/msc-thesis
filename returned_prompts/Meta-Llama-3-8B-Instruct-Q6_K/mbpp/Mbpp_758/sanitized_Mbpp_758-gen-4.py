def unique_sublists(lst):
    freq = {}
    for sublist in lst:
        sublist = tuple(sublist)
        if sublist in freq:
            freq[sublist] += 1
        else:
            freq[sublist] = 1
    return freq