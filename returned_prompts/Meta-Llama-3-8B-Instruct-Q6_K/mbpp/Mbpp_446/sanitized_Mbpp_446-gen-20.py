def count_Occurrence(t, lst):
    from collections import Counter
    t = tuple(t)
    lst = tuple(lst)
    return sum(Counter(t)[i] for i in lst)