def interleave_lists(list1, list2, list3):
    return [j for i in zip(list1, list2, list3) for j in i]