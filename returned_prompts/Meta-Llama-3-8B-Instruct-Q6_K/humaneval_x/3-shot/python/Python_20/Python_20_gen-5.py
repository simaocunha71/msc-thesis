    min_diff = float('inf')
    closest_pair = (float('inf'), float('inf'))

    for idx, elem in enumerate(numbers):
        for idx2, elem2 in enumerate(numbers):
            if idx != idx2:
                diff = abs(elem - elem2)
                if diff < min_diff:
                    min_diff = diff
                    closest_pair = (min(elem, elem2), max(elem, elem2))

    return closest_pair


