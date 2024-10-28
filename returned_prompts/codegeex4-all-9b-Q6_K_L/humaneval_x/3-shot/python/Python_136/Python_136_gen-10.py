    negative_nums = [i for i in lst if i < 0]
    positive_nums = [i for i in lst if i > 0]

    if negative_nums:
        return (max(negative_nums), min(positive_nums))
    elif positive_nums:
        return (None, min(positive_nums))
    else:
        return (None, None)

