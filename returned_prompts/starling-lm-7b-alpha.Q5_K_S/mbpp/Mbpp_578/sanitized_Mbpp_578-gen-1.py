def interleave_lists(l1, l2, l3):
    return [x for i in range(len(l1)) for x in [l1[i], l2[i], l3[i]]]