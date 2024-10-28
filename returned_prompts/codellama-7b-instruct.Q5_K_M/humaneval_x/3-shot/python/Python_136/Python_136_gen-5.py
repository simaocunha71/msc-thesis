    max_negative = max([x for x in lst if x < 0], default=None)
    min_positive = min([x for x in lst if x > 0], default=None)

    return (max_negative, min_positive)
