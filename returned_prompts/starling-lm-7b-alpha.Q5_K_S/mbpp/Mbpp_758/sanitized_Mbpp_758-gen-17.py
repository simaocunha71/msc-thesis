def unique_sublists(list_):
    d = {}
    for sublist in list_:
        sublist_tuple = tuple(sublist)
        if sublist_tuple not in d:
            d[sublist_tuple] = 1
        else:
            d[sublist_tuple] += 1
    return d