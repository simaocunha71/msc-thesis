def unique_sublists(lst):
    counts = {}
    for sublist in lst:
        tup = tuple(sublist)
        if tup in counts:
            counts[tup] += 1
        else:
            counts[tup] = 1
    return counts