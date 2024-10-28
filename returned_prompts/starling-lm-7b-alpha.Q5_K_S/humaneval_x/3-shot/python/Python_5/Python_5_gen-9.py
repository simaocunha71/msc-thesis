    result = []
    for idx, elem in enumerate(numbers[:-1]):
        result.append(elem)
        result.append(delimeter)
    result.append(numbers[-1])
    return result


