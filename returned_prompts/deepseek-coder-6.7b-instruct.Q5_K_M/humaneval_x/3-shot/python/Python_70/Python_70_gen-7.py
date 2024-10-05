    lst.sort()
    result = []
    while lst:
        result.append(lst.pop(0))  # remove and append the smallest
        if lst:
            result.append(lst.pop())  # remove and append the largest
    return result


