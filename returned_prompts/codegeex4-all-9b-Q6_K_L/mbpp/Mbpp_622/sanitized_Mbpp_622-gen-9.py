def get_median(list1, list2, n):
    merged_list = sorted(list1 + list2)
    median = merged_list[n // 2] if n % 2 == 1 else (merged_list[n // 2 - 1] + merged_list[n // 2]) / 2
    return median