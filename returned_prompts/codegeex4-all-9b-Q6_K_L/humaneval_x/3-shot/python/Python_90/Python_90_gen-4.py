    if len(lst) < 2:
        return None

    lst.sort()
    for i in range(len(lst) - 1):
        if lst[i] != lst[i + 1]:
            return lst[i + 1]

    return None

