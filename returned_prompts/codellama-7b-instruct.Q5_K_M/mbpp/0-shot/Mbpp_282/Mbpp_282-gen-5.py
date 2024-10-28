def sub_list(list1, list2):
    assert len(list1) == len(list2)
    return [i - j for i, j in zip(list1, list2)]

