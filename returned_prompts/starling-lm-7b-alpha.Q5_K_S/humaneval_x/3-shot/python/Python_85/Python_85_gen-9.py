    result = 0
    for idx, elem in enumerate(lst):
        if elem % 2 == 0 and idx % 2 == 1:
            result += elem
    return result


