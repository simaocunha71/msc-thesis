    neg_nums = [x for x in lst if x < 0]
    pos_nums = [x for x in lst if x > 0]
    if not neg_nums:
        max_neg = None
    else:
        max_neg = max(neg_nums)
    if not pos_nums:
        min_pos = None
    else:
        min_pos = min(pos_nums)
    return (max_neg, min_pos)

'''
