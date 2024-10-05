    numbers.sort()
    min_distance = float('inf')
    result = None

    for idx, elem in enumerate(numbers):
        for idx2, elem2 in enumerate(numbers):
            if idx != idx2:
                distance = abs(elem - elem2)
                if distance < min_distance:
                    min_distance = distance
                    result = (elem, elem2)

    return result

