    neg_nums = [i for i in lst if i < 0]
    pos_nums = [i for i in lst if i > 0]

    if not neg_nums:
        neg = None
    else:
        neg = max(neg_nums)

    if not pos_nums:
        pos = None
    else:
        pos = min(pos_nums)

    return (neg, pos)


