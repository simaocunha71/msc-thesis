    seen = set()
    result = []
    for elem in numbers:
        if elem not in seen:
            seen.add(elem)
            result.append(elem)

    return result


