    largest_negative = None
    smallest_positive = None
    for elem in lst:
        if elem < 0 and (largest_negative is None or elem > largest_negative):
            largest_negative = elem
        if elem > 0 and (smallest_positive is None or elem < smallest_positive):
            smallest_positive = elem
    return largest_negative, smallest_positive


