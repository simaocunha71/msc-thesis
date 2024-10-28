    result = 0
    for i, elem in enumerate(lst):
        if i % 3 == 0:
            result += elem ** 2
        elif i % 4 == 0 and i % 3 != 0:
            result += elem ** 3

    return result


