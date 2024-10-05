    result = 0
    for idx, elem in enumerate(lst):
        if idx % 2 == 0:
            if elem % 2 == 1:
                result += elem
    return result


