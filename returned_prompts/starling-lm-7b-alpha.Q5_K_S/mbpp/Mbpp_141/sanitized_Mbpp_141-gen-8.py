def pancake_sort(lst):
    for i in range(len(lst) // 2):
        max_idx = lst.index(max(lst[:len(lst) - i - 1]))
        lst.pop(max_idx)
        lst.insert(0, max(lst[:len(lst) - i - 1]))
    return lst