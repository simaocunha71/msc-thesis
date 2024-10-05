    result = []
    current_max = float('-inf')

    for number in numbers:
        current_max = max(current_max, number)
        result.append(current_max)

    return result

