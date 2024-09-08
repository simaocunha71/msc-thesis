def get_median(list1, list2, n):
    merged = sorted(list1 + list2)
    return (merged[n-1] + merged[n]) / 2.0