    pos_int = None
    neg_int = None
    for num in lst:
        if num > 0:
            if pos_int is None:
                pos_int = num
            elif num > pos_int:
                pos_int = num
        elif num < 0:
            if neg_int is None:
                neg_int = num
            elif num < neg_int:
                neg_int = num
    return (neg_int, pos_int)


