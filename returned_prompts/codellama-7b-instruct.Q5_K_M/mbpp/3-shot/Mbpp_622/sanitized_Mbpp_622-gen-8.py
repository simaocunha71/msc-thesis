def get_median(list1: list, list2: list, size: int) -> float:
    median = 0.0
    if size % 2 == 0:
        median = (list1[size // 2 - 1] + list2[size // 2 - 1] + list1[size // 2] + list2[size // 2]) / 4
    else:
        median = (list1[size // 2] + list2[size // 2]) / 2
    return median