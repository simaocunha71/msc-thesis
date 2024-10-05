    numbers.sort()
    min_diff = float('inf')
    closest_pair = (None, None)

    for idx in range(1, len(numbers)):
        diff = numbers[idx] - numbers[idx-1]
        if diff < min_diff:
            min_diff = diff
            closest_pair = (numbers[idx-1], numbers[idx])

    return closest_pair


