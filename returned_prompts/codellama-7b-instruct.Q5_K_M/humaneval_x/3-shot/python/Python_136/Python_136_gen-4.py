    max_neg = max([i for i in lst if i < 0], default=None)
    min_pos = min([i for i in lst if i > 0], default=None)

    return (max_neg, min_pos)


