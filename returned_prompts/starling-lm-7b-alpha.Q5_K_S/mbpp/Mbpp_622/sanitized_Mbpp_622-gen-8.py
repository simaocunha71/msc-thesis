def merge_sorted_lists(list1, list2):
    merged_list = list1 + list2
    merged_list.sort()
    return merged_list
def get_median(list1, list2, k):
    merged_list = merge_sorted_lists(list1, list2)
    middle_index = len(merged_list) // 2

    if len(merged_list) % 2 == 0:
        return (merged_list[middle_index - 1] + merged_list[middle_index]) / 2.0
    else:
        return merged_list[middle_index]
list1 = [1, 12, 15, 26, 38]
list2 = [2, 13, 17, 30, 45]
k = 5