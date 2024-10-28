def get_median(list1: list, list2: list, length: int) -> float:
    combined_list = list1 + list2
    combined_list.sort()
    median = 0
    if length % 2 == 0:
        median = (combined_list[length // 2 - 1] + combined_list[length // 2]) / 2
    else:
        median = combined_list[length // 2]
    return median

