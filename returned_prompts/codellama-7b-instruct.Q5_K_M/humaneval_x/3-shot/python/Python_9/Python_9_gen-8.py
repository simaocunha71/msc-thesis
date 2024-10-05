    result = []
    current_max = 0

    for idx, num in enumerate(numbers):
        current_max = max(num, current_max)
        result.append(current_max)

    return result


