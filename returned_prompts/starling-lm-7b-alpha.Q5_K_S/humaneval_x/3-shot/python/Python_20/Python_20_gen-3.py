    min_distance = float('inf')
    min_pair = None

    for idx, elem in enumerate(numbers):
        for idx2, elem2 in enumerate(numbers):
            if idx != idx2:
                distance = abs(elem - elem2)
                if distance < min_distance:
                    min_distance = distance
                    min_pair = (elem, elem2)

    return min_pair


