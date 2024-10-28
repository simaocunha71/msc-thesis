    min_diff = float('inf')
    closest_pair = None

    for idx, elem in enumerate(numbers):
        for idx2, elem2 in enumerate(numbers):
            diff = abs(elem - elem2)
            if diff < min_diff:
                min_diff = diff
                closest_pair = (numbers[idx], numbers[idx2])

    return closest_pair


