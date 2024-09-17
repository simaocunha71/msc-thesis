def interleave_lists(list1, list2, list3):
    return [x for i in range(len(list1)) for x in [list1[i], list2[i], list3[i]]]