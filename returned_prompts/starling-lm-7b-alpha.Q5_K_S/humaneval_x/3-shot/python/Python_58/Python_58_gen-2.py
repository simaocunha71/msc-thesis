    result = []
    for elem in l1:
        if elem in l2 and elem not in result:
            result.append(elem)
    return result


