    closest_pair = None
    closest_distance = None

    for idx, elem in enumerate(numbers):
        for idx2, elem2 in enumerate(numbers):
            if idx != idx2:
                distance = abs(elem - elem2)
                if closest_pair is None or distance < closest_distance:
                    closest_pair = (elem, elem2)
                    closest_distance = distance

    return closest_pair


