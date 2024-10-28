    min_diff = float('inf')
    min_pair = None

    for i in range(len(numbers)):
        for j in range(i + 1, len(numbers)):
            diff = abs(numbers[i] - numbers[j])
            if diff < min_diff:
                min_diff = diff
                min_pair = (min(numbers[i], numbers[j]), max(numbers[i], numbers[j]))

    return min_pair

