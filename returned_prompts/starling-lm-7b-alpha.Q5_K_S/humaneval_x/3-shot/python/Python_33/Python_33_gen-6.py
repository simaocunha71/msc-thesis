    thirds = [index for index in range(len(l)) if index % 3 == 0]
    other = [index for index in range(len(l)) if index % 3 != 0]

    thirds.sort(key=lambda index: l[index])
    result = l.copy()

    for idx in thirds:
        result[idx] = l[thirds[idx]]

    return result


