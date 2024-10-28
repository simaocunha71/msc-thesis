    negatives = [x for x in lst if x < 0]
    positives = [x for x in lst if x > 0]

    if negatives:
        largest_negative = max(negatives)
    else:
        largest_negative = None

    if positives:
        smallest_positive = min(positives)
    else:
        smallest_positive = None

    return (largest_negative, smallest_positive)

