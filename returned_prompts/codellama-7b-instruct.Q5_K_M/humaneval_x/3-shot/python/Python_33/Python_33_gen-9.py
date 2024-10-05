    result = []

    for i in range(0, len(l), 3):
        result.append(l[i])

    result.sort()

    for i in range(1, len(l), 3):
        result.append(l[i])

    for i in range(2, len(l), 3):
        result.append(l[i])

    return result


