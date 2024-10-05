    result = []
    for idx in range(1, n+1):
        if idx % 2 == 0:
            result.append(idx + 1)
        else:
            result.append(idx + 2)
    return result


