    result = []
    for num in numbers:
        result.append(num)
        result.append(delimeter)

    if len(result) > 1:
        result.pop()

    return result


