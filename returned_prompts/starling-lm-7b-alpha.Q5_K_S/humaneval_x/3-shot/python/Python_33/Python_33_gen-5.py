    result = []
    for index, elem in enumerate(l):
        if index % 3 != 0:
            result.append(elem)
        else:
            result.append(sorted(elem)[0])
    return result


