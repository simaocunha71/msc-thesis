    result = []
    for index, elem in enumerate(lst):
        if index % 2 == 0 and elem % 2 == 0:
            result.append(elem)
    return result


