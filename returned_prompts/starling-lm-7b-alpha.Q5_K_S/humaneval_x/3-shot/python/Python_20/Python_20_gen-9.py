    min_distance = float('inf')
    min_indexes = (0, 1)

    for idx, elem1 in enumerate(numbers):
        for idx2, elem2 in enumerate(numbers):
            if idx != idx2:
                distance = abs(elem1 - elem2)
                if distance < min_distance:
                    min_distance = distance
                    min_indexes = (idx, idx2)

    return numbers[min_indexes[0]], numbers[min_indexes[1]]


