    lst.sort()
    result = []
    while lst:
        result.append(lst[0])
        lst.pop(lst.index(lst[0]))
        lst.sort(reverse=True)
    return result


