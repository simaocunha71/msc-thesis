    result = []
    max_elem = numbers[0]

    for elem in numbers:
        max_elem = max(max_elem, elem)
        result.append(max_elem)

    return result


