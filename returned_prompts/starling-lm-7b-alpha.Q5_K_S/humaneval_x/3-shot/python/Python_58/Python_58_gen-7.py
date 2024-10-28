    result = []
    for i in l1:
        if i in l2 and i not in result:
            result.append(i)
    return result


