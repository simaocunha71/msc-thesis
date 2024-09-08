def pancake_sort(lst):
    for i in range(len(lst), 0, -1):
        max_index = lst[0:i].index(max(lst[0:i]))
        if max_index != i - 1:
            lst[0:i] = lst[0:i][::-1]
            lst[0:i] = lst[0:i][::-1]
    return lst