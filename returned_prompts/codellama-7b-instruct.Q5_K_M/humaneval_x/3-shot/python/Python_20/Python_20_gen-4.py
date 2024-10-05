    closest_pair = None
    for idx, elem in enumerate(numbers):
        for idx2, elem2 in enumerate(numbers):
            if idx != idx2:
                if closest_pair is None:
                    closest_pair = (elem, elem2)
                else:
                    distance = abs(elem - elem2)
                    if distance < abs(closest_pair[0] - closest_pair[1]):
                        closest_pair = (elem, elem2)

    return closest_pair


