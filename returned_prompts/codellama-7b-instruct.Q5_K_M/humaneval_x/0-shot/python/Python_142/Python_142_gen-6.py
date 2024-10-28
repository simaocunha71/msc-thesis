
    result = 0
    for index, value in enumerate(lst):
        if index % 3 == 0:
            result += value ** 3
        elif index % 4 == 0 and index % 3 != 0:
            result += value ** 2
    return result
