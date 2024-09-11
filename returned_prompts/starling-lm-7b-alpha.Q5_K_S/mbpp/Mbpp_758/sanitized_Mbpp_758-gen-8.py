def unique_sublists(list_):
    from collections import defaultdict
    dic = defaultdict(int)
    for sublist in list_:
        tup = tuple(sublist)
        dic[tup] += 1
    return dict(dic)