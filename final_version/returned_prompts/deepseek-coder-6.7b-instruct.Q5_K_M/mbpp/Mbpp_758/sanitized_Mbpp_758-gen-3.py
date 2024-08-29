def unique_sublists(lst):
    dic = {}
    for sublist in lst:
        tup = tuple(sublist)
        if tup in dic:
            dic[tup] += 1
        else:
            dic[tup] = 1
    return dic