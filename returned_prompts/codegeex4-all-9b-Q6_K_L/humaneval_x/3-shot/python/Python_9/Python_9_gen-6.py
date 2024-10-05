    result = []

    for idx, number in enumerate(numbers):
        result.append(max(numbers[:idx+1]))

    return result


