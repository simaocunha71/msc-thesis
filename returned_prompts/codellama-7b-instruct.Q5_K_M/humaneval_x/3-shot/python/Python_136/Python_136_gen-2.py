    largest_negative = None
    smallest_positive = None

    for i in lst:
        if i < 0:
            largest_negative = max(largest_negative, i) if largest_negative else i
        elif i > 0:
            smallest_positive = min(smallest_positive, i) if smallest_positive else i

    return (largest_negative, smallest_positive)


