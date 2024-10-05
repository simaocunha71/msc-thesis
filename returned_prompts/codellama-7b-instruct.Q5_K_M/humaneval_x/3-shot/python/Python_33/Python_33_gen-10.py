    result = []

    for idx, elem in enumerate(l):
        if idx % 3 == 0:
            result.append(elem)

    result.sort()

    for idx, elem in enumerate(l):
        if idx % 3 != 0:
            result.append(elem)

    return result


