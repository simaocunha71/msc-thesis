    if not lst:
        return []

    lst.sort()
    result = [lst[0]]
    lst.pop(0)
    lst.sort(reverse=True)
    result.append(lst[0])
    lst.pop(0)

    while lst:
        result.append(lst[0])
        lst.pop(0)
        lst.sort()
        result.append(lst[0])
        lst.pop(0)

    return result


