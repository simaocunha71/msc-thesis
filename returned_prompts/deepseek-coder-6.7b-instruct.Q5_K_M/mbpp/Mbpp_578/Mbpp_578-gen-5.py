
def interleave_lists(l1, l2, l3):
    return [val for pair in zip(l1, l2, l3) for val in pair]


