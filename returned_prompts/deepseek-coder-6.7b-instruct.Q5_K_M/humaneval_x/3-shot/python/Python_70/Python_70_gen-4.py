    lst.sort()
    result = []
    while len(lst) > 0:
        result.append(lst.pop(0))
        if len(lst) > 0:
            result.append(lst.pop())
    return result


