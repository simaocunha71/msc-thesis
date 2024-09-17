
def interleave_lists(lst1, lst2, lst3):
    return [val for pair in zip(lst1, lst2, lst3) for val in pair]


