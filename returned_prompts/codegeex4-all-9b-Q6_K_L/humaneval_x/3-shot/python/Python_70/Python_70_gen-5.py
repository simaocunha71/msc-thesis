    result = []
    while lst:
        lst.sort()
        result.append(lst.pop(0))
        if lst:
            result.append(lst.pop())

    return result

