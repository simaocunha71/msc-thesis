def pancake_sort(lst):
    lst = list(lst)
    for i in range(len(lst) - 1, -1, -1):
        for j in range(len(lst) - 1, -1, -1):
            if lst[j] < lst[i]:
                lst[j], lst[i] = lst[i], lst[j]
        lst = lst[i + 1:]
    return lst