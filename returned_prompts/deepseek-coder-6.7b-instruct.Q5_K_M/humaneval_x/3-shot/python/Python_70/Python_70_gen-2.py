    lst.sort()
    result = []
    while lst:
        result.append(lst.pop(0))  # pop smallest
        if lst:  # if there are still elements
            result.append(lst.pop())  # pop largest
    return result


