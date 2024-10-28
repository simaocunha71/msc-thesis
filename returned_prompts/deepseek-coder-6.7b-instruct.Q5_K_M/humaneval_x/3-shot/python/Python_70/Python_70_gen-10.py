    lst.sort()
    result = []
    while lst:
        result.append(lst.pop(0))  # remove and append min
        if lst:
            result.append(lst.pop())  # remove and append max
    return result


