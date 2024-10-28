    result = []
    for idx, elem in enumerate(lst):
        if idx % 2 == 0 and elem % 2 == 0:
            result.append(elem)

    return sum(result)


