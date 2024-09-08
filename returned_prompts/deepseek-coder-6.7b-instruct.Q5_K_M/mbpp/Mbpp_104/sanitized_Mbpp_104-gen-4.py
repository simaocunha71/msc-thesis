def sort_sublists(lst):
    for i in range(len(lst)):
        lst[i] = sorted(lst[i])
    return lst