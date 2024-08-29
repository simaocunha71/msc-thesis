
def get_median(list1, list2, n):
    merged = sorted(list1 + list2)
    return (merged[n-1] + merged[n]) / 2.0

assert get_median([1, 12, 15, 26, 38], [2, 13, 17, 30, 45], 5) == 16.0

