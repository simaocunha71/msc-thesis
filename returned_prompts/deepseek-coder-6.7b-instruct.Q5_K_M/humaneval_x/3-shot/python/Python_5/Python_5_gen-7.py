    result = []
    for idx, num in enumerate(numbers):
        result.append(num)
        if idx != len(numbers) - 1:
            result.append(delimeter)
    return result


