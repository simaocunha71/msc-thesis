    closest_pair = (numbers[0], numbers[1])
    for idx, elem in enumerate(numbers):
        for idx2, elem2 in enumerate(numbers):
            if idx != idx2:
                if abs(elem - elem2) < abs(closest_pair[0] - closest_pair[1]):
                    closest_pair = (elem, elem2)

    return closest_pair


