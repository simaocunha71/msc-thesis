    result = 0
    for elem in lst:
        if isinstance(elem, int) and elem > 0:
            result += (elem**2)

    return result


