    result = []
    for elem in l:
        if elem % 3 == 0:
            result.append(sorted(elem))
        else:
            result.append(elem)

    return result


