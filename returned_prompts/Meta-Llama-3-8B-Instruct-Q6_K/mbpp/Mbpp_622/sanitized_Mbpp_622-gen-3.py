def get_median(list1, list2, size):
    merged_list = sorted(list1 + list2)
    median = merged_list[size // 2] if size % 2 != 0 else (merged_list[size // 2 - 1] + merged_list[size // 2]) / 2
    return median