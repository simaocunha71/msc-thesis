    positive_nums = [n for n in lst if n > 0]
    negative_nums = [n for n in lst if n < 0]

    if not positive_nums:
        positive_nums = [None]
    else:
        positive_nums = [min(positive_nums)]

    if not negative_nums:
        negative_nums = [None]
    else:
        negative_nums = [max(negative_nums)]

    return tuple(negative_nums + positive_nums)

