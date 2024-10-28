    if len(lst) == 1:
        return True
    if len(lst) == 2:
        return lst[0] != lst[1]
    if len(lst) == 3:
        return lst[0] < lst[1] < lst[2]
    for i in range(len(lst) - 1):
        if lst[i] > lst[i + 1]:
            return False
    return True


