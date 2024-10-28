    neg_nums = [x for x in lst if x < 0]
    pos_nums = [x for x in lst if x > 0]

    if not neg_nums:
        a = None
    else:
        a = max(neg_nums)

    if not pos_nums:
        b = None
    else:
        b = min(pos_nums)

    return (a, b)


