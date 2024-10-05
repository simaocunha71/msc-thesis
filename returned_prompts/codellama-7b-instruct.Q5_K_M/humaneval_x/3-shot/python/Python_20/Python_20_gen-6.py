    min_distance = float('inf')
    first_closest = None
    second_closest = None

    for idx, elem in enumerate(numbers):
        for idx2, elem2 in enumerate(numbers):
            if idx != idx2:
                distance = abs(elem - elem2)
                if distance < min_distance:
                    min_distance = distance
                    first_closest = elem
                    second_closest = elem2

    return first_closest, second_closest
