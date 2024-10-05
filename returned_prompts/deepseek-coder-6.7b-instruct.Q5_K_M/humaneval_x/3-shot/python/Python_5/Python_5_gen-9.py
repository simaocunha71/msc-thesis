    result = []
    for idx, elem in enumerate(numbers):
        result.append(elem)
        if idx != len(numbers) - 1:
            result.append(delimeter)
    return result


