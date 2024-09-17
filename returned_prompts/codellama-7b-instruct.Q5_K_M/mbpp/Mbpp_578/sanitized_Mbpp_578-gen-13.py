def interleave_lists(list1, list2, list3):
    assert len(list1) == len(list2) == len(list3)
    result = []
    for i in range(len(list1)):
        result += [list1[i], list2[i], list3[i]]
    return result