    if not numbers:
        return []

    result = []
    result.append(numbers[0])

    for i in range(1, len(numbers)):
        result.append(delimeter)
        result.append(numbers[i])

    return result

