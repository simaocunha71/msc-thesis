    negatives = [x for x in lst if x < 0]
    positives = [x for x in lst if x > 0]

    if not negatives:
        negatives = [None]
    else:
        negatives = [min(negatives)]

    if not positives:
        positives = [None]
    else:
        positives = [max(positives)]

    return tuple(negatives + positives)

