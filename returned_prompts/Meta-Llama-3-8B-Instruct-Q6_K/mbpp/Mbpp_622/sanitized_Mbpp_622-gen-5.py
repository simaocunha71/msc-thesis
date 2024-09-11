def get_median(list1, list2, n):
    sorted_list = sorted(list1 + list2)
    return sorted_list[n//2] if n % 2 != 0 else (sorted_list[n//2 - 1] + sorted_list[n//2]) / 2