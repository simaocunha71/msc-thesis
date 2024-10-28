    result = []
    seen = {}
    for elem in numbers:
        if elem not in seen:
            seen[elem] = True
            result.append(elem)
    return result


