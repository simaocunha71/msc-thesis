def pancake_sort(lst: list) -> list:
    for i in range(len(lst), 0, -1):
        max_idx = lst[0:i].index(max(lst[0:i]))
        if max_idx != i - 1:
            lst[0:i] = lst[max_idx::-1] + lst[i:]
    return lst