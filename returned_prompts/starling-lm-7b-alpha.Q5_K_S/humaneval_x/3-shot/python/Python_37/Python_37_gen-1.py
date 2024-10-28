    result = []
    for i in range(0, len(l), 2):
        result.append(l[i])
    for i in range(1, len(l), 2):
        result.append(sorted(l[i:i+2])[0])

    return result


