    closest_pair = [0.0, 0.0]
    closest_diff = 100000.0

    for idx, elem in enumerate(numbers):
        for idx2, elem2 in enumerate(numbers):
            if idx != idx2 and abs(elem - elem2) < closest_diff:
                closest_diff = abs(elem - elem2)
                closest_pair[0] = elem
                closest_pair[1] = elem2

    return tuple(closest_pair)


