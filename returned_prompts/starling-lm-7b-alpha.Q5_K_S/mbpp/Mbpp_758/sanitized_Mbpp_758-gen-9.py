def unique_sublists(lst):
    from collections import defaultdict
    d = defaultdict(int)
    for i in lst:
        tmp = tuple(i)
        d[tmp]+=1
    return dict(d)