    result = []
    current_max = 0

    for i in range(len(numbers)):
        current_max = max(current_max, numbers[i])
        result.append(current_max)

    return result


