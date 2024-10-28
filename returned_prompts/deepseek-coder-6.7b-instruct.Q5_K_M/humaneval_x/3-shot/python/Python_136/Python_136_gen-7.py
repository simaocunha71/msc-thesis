    neg_nums = [num for num in lst if num < 0]
    pos_nums = [num for num in lst if num > 0]

    if neg_nums:
        a = max(neg_nums)
    else:
        a = None

    if pos_nums:
        b = min(pos_nums)
    else:
        b = None

    return a, b


