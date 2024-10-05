    result = 0
    for idx, elem in enumerate(lst):
        if idx % 2 == 0 and elem % 2 != 0:
            result += elem
    return result


