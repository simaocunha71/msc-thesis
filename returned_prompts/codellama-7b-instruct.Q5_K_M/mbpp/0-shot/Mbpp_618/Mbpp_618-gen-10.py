def div_list(list1, list2):
    assert len(list1)==len(list2)
    return [l1/l2 for l1, l2 in zip(list1, list2)]
