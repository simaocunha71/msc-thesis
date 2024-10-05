    result = 0
    for idx, val in enumerate(lst):
        if idx % 3 == 0:
            result += val ** 2
        elif idx % 4 == 0 and idx % 3 != 0:
            result += val ** 3
    return result
