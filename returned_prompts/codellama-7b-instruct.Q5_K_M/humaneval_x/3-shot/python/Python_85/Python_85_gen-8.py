    result = 0
    for idx, elem in enumerate(lst):
        if idx % 2 == 1 and elem % 2 == 0:
            result += elem

    return result


