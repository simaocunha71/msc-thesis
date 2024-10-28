

def get_median(list1, list2):
    assert len(list1) == len(list2)
    mid = len(list1) // 2
    return (list1[mid] + list2[mid]) / 2


def get_median(list1, list2, k):
    assert len(list1) == len(list2)
    if k % 2 == 0:
        return (list1[k // 2 - 1] + list2[k // 2 - 1]) / 2
    else:
        return (list1[k // 2] + list2[k // 2]) / 2
