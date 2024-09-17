
def pancake_sort(lst):
    for i in range(len(lst), 0, -1):
        max_idx = lst[0:i].index(max(lst[0:i]))
        if max_idx != i-1:
            if max_idx != 0:
                lst[0:max_idx+1] = reversed(lst[0:max_idx+1])
            lst[0:i] = reversed(lst[0:i])
    return lst


