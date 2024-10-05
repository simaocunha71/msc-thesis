    result = []
    for i, elem in enumerate(numbers):
        result.append(elem)
        if i < len(numbers) - 1:
            result.append(delimeter)

    return result


