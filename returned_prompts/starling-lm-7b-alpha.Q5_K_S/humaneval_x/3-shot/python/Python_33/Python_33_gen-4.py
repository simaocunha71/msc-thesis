    result = []
    for elem in l:
        if elem % 3 != 0:
            result.append(elem)
        else:
            result.append(sorted(elem)[0])
    return result


