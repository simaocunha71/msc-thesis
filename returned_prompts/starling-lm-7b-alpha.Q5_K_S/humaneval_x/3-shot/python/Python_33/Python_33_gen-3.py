    result = []
    for idx, elem in enumerate(l):
        if idx % 3 != 0:
            result.append(elem)
        else:
            result.append(sorted(elem))

    return result


