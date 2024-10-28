    result = []
    for i in x:
        if all(j % 2 != 0 for j in str(i)):
            result.append(i)
    return sorted(result)


