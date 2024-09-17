def combinations_list(lst):
    return [[x for i, x in enumerate(lst) if (i & k) == i] for k in range(1 << len(lst))]