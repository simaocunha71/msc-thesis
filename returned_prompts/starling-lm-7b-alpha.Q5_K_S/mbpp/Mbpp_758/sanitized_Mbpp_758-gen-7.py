def unique_sublists(lst):
    lst = sorted(lst)
    return {frozenset(lst[i:j]): j - i for i, j in zip(range(len(lst)), lst[1:])}