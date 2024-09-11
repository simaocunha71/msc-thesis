def interleave_lists(list1, list2, list3):
    return [x for t in zip(list1, list2, list3) for x in t]  # using list comprehension and zip function