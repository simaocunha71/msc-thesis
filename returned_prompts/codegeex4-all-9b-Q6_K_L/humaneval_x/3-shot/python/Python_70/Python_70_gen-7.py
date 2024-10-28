    if not lst:
        return []

    lst.sort()
    result = []

    while lst:
        result.append(lst.pop(0))
        if lst:
            result.append(lst.pop())

    return result

