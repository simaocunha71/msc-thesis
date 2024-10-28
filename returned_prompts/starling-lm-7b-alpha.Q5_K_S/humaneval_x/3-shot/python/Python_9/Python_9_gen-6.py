    result = [float('-inf')] * len(numbers)
    max_elem = float('-inf')

    for idx, elem in enumerate(numbers):
        result[idx] = max(max_elem, elem)
        max_elem = max(max_elem, elem)

    return result


