    result = []
    current_max = 0

    for num in numbers:
        current_max = max(num, current_max)
        result.append(current_max)

    return result


