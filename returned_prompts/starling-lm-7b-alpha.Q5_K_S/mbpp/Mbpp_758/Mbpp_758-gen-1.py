
def unique_sublists(lst):
    d = {}
    for sublist in lst:
        t = tuple(sublist)
        if t not in d:
            d[t] = 1
        else:
            d[t] += 1
    return d


