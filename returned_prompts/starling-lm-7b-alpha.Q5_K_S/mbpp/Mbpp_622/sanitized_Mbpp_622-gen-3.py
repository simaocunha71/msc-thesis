def get_median(list1, list2, size):
    merged_list = sorted(list1 + list2)
    return merged_list[size//2]
list1 = [1, 12, 15, 26, 38]
list2 = [2, 13, 17, 30, 45]
size = 5