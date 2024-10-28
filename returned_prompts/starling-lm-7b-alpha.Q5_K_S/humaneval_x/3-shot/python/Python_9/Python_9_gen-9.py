    result = []
    max_elem = max(numbers[:])
    for elem in numbers:
        if max_elem == elem:
            result.append(max_elem)
        else:
            result.append(max_elem)
            max_elem = elem

    return result


