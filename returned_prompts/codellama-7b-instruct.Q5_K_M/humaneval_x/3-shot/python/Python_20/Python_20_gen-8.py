    closest_pair = (None, None)
    closest_diff = None

    for idx, elem in enumerate(numbers):
        for idx2, elem2 in enumerate(numbers):
            if idx != idx2:
                diff = abs(elem - elem2)
                if closest_diff is None or diff < closest_diff:
                    closest_diff = diff
                    closest_pair = (elem, elem2)

    return closest_pair


