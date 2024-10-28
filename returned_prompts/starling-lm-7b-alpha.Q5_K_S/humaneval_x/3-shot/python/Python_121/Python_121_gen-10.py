    result = 0
    for idx, elem in enumerate(lst):
        if elem % 2 == 0 and idx % 2 == 0:
            result += elem

    return result


