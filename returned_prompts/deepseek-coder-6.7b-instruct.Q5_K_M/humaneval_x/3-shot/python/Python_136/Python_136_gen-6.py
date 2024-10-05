    largest_negative = None
    smallest_positive = None
    for n in lst:
        if n < 0:
            if largest_negative is None or n > largest_negative:
                largest_negative = n
        elif n > 0:
            if smallest_positive is None or n < smallest_positive:
                smallest_positive = n
    return largest_negative, smallest_positive


