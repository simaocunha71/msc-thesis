    result = []
    current_max = float('-inf')

    for n in numbers:
        current_max = max(current_max, n)
        result.append(current_max)

    return result


