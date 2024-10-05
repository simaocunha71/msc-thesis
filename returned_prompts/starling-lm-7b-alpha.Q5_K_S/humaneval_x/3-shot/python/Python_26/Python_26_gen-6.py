    seen = set()
    result = []
    for elem in numbers:
        if elem not in seen:
            result.append(elem)
            seen.add(elem)
    return result


