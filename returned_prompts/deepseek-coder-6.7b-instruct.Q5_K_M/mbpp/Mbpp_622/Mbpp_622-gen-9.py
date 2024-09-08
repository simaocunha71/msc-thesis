def get_median(list1, list2, n):
    merged_list = sorted(list1 + list2)
    return (merged_list[n - 1] + merged_list[n]) / 2

print(get_median([1, 12, 15, 26, 38], [2, 13, 17, 30, 45], 5))

