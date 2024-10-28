    if len(lst) < 2:
        return None

    lst.sort()
    if lst[0] != lst[1]:
        return lst[1]
    else:
        for i in range(1, len(lst)):
            if lst[i] != lst[0]:
                return lst[i]
        return None


