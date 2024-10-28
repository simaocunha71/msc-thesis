    result = []
    for i in range(len(lst)):
        if lst[i] % 2 == 0 and i % 2 != 0:
            result.append(lst[i])

    return result


