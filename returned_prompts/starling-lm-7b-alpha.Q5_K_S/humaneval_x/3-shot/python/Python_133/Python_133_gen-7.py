    result = 0
    for elem in lst:
        elem_rounded = int(round(elem))
        result += elem_rounded ** 2
    return result


