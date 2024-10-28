    result = 0
    for i, elem in enumerate(lst):
        if elem % 2 == 0 and i % 2 == 0:
            result += elem

    return result


