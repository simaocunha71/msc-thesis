    if len(lst) < 2:
        return None

    first = lst[0]
    second = lst[1]

    for elem in lst[2:]:
        if elem < first:
            first = elem
        elif elem < second:
            second = elem

    return second


