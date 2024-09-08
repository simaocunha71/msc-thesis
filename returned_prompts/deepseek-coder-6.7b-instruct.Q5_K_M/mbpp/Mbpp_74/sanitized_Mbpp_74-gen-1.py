def is_samepatterns(lst1, lst2):
    return lst1 == [x for i, x in enumerate(lst2) for _ in range(lst1.index(x)+1 if x in lst1[:i] else 1)]