    if not lst:
        return lst

    lst.sort()
    result = []
    while lst:
        result.append(lst.pop(0))
        if lst:
            lst.sort(reverse=True)
            result.append(lst.pop(0))
    return result


