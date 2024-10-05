    negatives = [x for x in lst if x < 0]
    positives = [x for x in lst if x > 0]

    if not negatives:
        negatives = [None]
    if not positives:
        positives = [None]

    return max(negatives), min(positives)

