def get_median(list1, list2):
    assert len(list1) == len(list2)
    mid = len(list1) // 2
    return (list1[mid] + list2[mid]) / 2