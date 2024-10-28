    result = 0
    for idx, elem in enumerate(lst):
        if idx % 3 == 0:
            elem = elem ** 2
        elif idx % 4 == 0 and idx % 3 != 0:
            elem = elem ** 3
        result += elem
    return result


