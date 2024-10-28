    if not lst:
        return []

    result = []
    lst.sort()
    while lst:
        result.append(lst.pop(0))
        if lst:
            result.append(lst.pop())

    return result

