    max_neg_val = None
    min_pos_val = None
    for elem in lst:
        if elem < 0:
            if max_neg_val is None or elem > max_neg_val:
                max_neg_val = elem
        elif elem > 0:
            if min_pos_val is None or elem < min_pos_val:
                min_pos_val = elem
    return max_neg_val, min_pos_val


