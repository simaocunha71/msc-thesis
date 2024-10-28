def get_median(list1, list2, n):
    combined_list = sorted(list1 + list2)
    median = combined_list[n//2] if n % 2 != 0 else (combined_list[n//2 - 1] + combined_list[n//2]) / 2
    return median