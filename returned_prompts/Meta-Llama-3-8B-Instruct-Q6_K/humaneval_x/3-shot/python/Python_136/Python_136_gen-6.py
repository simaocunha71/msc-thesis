    max_negative = max([num for num in lst if num < 0], default=None)
    min_positive = min([num for num in lst if num > 0], default=None)

    return max_negative, min_positive


