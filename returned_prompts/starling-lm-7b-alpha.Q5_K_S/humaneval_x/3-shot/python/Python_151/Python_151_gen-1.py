    result = 0
    for elem in lst:
        if elem % 2 != 0 and isinstance(elem, int):
            result += (elem ** 2)
    return result


