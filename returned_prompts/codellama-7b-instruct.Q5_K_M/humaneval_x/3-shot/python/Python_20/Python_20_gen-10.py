    closest_diff = float("inf")
    closest_pair = []

    for idx, elem in enumerate(numbers):
        for idx2, elem2 in enumerate(numbers):
            if idx != idx2:
                diff = abs(elem - elem2)
                if diff < closest_diff:
                    closest_diff = diff
                    closest_pair = [elem, elem2]

    return tuple(closest_pair)


