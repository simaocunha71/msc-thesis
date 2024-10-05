    min_diff = float("inf")
    first_closest = None
    second_closest = None

    for idx, elem in enumerate(numbers):
        for idx2, elem2 in enumerate(numbers):
            if idx != idx2:
                diff = abs(elem - elem2)
                if diff < min_diff:
                    min_diff = diff
                    first_closest = elem
                    second_closest = elem2

    return first_closest, second_closest


