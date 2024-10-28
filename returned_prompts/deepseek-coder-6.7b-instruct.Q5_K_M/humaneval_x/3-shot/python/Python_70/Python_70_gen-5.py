    lst.sort()
    result = []
    while lst:
        result.append(lst.pop(0)) # get smallest
        if lst: # if there are still elements left
            result.append(lst.pop()) # get largest
    return result


