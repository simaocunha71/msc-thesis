def get_median(list1, list2, size):
    merged_list = sorted(list1 + list2)
    if size % 2 == 0:
        return (merged_list[size // 2 - 1] + merged_list[size // 2]) / 2
    else:
        return merged_list[size // 2]