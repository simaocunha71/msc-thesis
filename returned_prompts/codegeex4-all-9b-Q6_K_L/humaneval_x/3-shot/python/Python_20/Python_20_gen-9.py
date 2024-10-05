    min_distance = float('inf')
    result = None

    for i in range(len(numbers)):
        for j in range(i + 1, len(numbers)):
            distance = abs(numbers[i] - numbers[j])
            if distance < min_distance:
                min_distance = distance
                result = (min(numbers[i], numbers[j]), max(numbers[i], numbers[j]))

    return result

