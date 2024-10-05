    result = []
    max_number = float('-inf')

    for elem in numbers:
        max_number = max(elem, max_number)
        result.append(max_number)

    return result


