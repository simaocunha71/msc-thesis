    min_diff = float('inf')
    closest_pair = (None, None)

    for i in range(len(numbers)):
        for j in range(i + 1, len(numbers)):
            diff = abs(numbers[i] - numbers[j])
            if diff < min_diff:
                min_diff = diff
                closest_pair = (numbers[i], numbers[j])

    return tuple(sorted(closest_pair))  # Sort the pair to ensure it's in order


