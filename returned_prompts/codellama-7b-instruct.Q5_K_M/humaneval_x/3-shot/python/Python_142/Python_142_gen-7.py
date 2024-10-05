    result = 0
    for idx, item in enumerate(lst):
        if idx % 3 == 0:
            result += item ** 2
        elif idx % 4 == 0 and idx % 3 != 0:
            result += item ** 3

    return result


