    if len(lst) == 0:
        return lst

    result = []
    lst.sort()
    result.append(lst[0])
    lst = lst[1:]

    while len(lst) > 0:
        lst.sort(reverse=True)
        result.append(lst[0])
        lst = lst[1:]

    return result

