def pancake_sort(lst):
    lst = lst.copy()
    for i in range(len(lst)):
        i = lst.index(min(lst[i:]))
        lst.pop(i)
        lst.insert(0, min(lst[i:]))
    return lst


