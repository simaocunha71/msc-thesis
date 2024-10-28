    result = []
    max_element = numbers[0]
    for elem in numbers:
        max_element = max(max_element, elem)
        result.append(max_element)

    return result


