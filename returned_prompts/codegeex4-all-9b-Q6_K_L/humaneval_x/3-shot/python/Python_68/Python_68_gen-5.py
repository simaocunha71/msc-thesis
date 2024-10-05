    result = []

    for index, value in enumerate(arr):
        if value % 2 == 0:
            result.append([value, index])

    if result:
        result.sort()
        return result[0]
    else:
        return result

