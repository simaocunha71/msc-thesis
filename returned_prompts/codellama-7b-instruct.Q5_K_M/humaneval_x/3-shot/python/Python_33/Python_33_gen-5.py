    result = []

    for i, x in enumerate(l):
        if i % 3 == 0:
            result.append(sorted(l[i:i + 3]))
        else:
            result.append(l[i])

    return result


