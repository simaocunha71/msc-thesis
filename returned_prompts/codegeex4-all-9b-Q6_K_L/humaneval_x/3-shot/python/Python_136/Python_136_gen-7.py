    negatives = [x for x in lst if x < 0]
    positives = [x for x in lst if x > 0]

    if not negatives:
        negatives = None
    else:
        negatives = max(negatives)

    if not positives:
        positives = None
    else:
        positives = min(positives)

    return negatives, positives

