    result = 0
    for idx, elem in enumerate(lst):
        if idx % 3 == 0:
            result += elem ** 2
        elif idx % 4 == 0 and idx % 3 != 0:
            result += elem ** 3
    return result


