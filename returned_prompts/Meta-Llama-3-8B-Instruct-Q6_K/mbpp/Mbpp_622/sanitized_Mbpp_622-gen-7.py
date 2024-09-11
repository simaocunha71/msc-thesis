def get_median(list1, list2, n):
    combined = sorted(list1 + list2)
    median = combined[n // 2] if n % 2 != 0 else (combined[n // 2 - 1] + combined[n // 2]) / 2
    return median