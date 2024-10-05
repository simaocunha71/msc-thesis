    result = 0

    for idx, x in enumerate(lst):
        if idx % 3 == 0:
            result += x ** 2
        elif idx % 4 == 0:
            result += x ** 3

    return result

