    closest_pair = (None, None)
    closest_diff = float('inf')

    for idx, elem in enumerate(numbers):
        for idx2, elem2 in enumerate(numbers):
            if idx != idx2:
                diff = abs(elem - elem2)

                if diff < closest_diff:
                    closest_pair = (elem, elem2)
                    closest_diff = diff

    return closest_pair


