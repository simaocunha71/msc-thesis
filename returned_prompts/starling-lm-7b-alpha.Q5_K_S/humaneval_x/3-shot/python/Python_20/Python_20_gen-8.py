    min_diff = float("inf")
    min_pair = (numbers[0], numbers[1])
    for idx, elem in enumerate(numbers):
        for idx2, elem2 in enumerate(numbers):
            if idx != idx2:
                diff = abs(elem - elem2)
                if diff < min_diff:
                    min_diff = diff
                    min_pair = (elem, elem2)

    return min_pair


