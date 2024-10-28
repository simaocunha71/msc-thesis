def pancake_sort(lst):
    for i in range(len(lst), 0, -1):
        max_idx = lst.index(max(lst[:i]))
        if max_idx != i - 1:
            if max_idx != 0:
                lst[:i] = lst[max_idx::-1] + lst[i:]
            lst[:i] = lst[::-1] + lst[i:]
    return lst