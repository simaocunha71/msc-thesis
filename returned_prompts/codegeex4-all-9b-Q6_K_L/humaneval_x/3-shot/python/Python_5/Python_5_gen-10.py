    result = []

    if len(numbers) > 0:
        result.append(numbers[0])

    for idx, elem in enumerate(numbers):
        if idx < len(numbers) - 1:
            result.append(delimeter)
            result.append(elem)

    return result

