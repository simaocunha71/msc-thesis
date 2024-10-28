    result = 0
    for elem in lst:
        if elem < 0:
            continue
        if elem % 2 != 0:
            result += (elem ** 2)
    return result


