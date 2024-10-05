    result = []
    for idx, elem in enumerate(l):
        if idx % 3 == 0:
            result.append(sorted(l[idx:idx + 3]))
        else:
            result.append(l[idx])

    return result


