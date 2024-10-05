    min_diff = float('inf')
    result = ()

    for idx, elem in enumerate(numbers):
        for idx2, elem2 in enumerate(numbers):
            if idx != idx2:
                diff = abs(elem - elem2)
                if diff < min_diff:
                    min_diff = diff
                    result = (elem, elem2)

    return result

