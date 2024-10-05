    result = 0
    for elem in lst:
        if isinstance(elem, int) and elem >= 0 and elem % 2 == 1:
            result += elem ** 2

    return result


