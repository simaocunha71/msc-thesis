def get_median(list1, list2, size):
    merged = sorted(list1 + list2)
    median = merged[size // 2] if size % 2 != 0 else (merged[size // 2 - 1] + merged[size // 2]) / 2
    return median