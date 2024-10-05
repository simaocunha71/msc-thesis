    max_negative = min_positive = None
    for elem in lst:
        if elem < 0:
            if max_negative is None or elem > max_negative:
                max_negative = elem
        elif elem > 0:
            if min_positive is None or elem < min_positive:
                min_positive = elem

    return max_negative, min_positive


