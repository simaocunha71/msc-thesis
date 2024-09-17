def unique_sublists(lst):
    from collections import defaultdict
    d = defaultdict(int)
    for sub in lst:
        sub_tuple = tuple(sub)
        d[sub_tuple] += 1
    return dict(d)