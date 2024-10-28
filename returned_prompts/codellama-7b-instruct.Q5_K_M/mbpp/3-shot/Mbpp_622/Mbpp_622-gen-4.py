
def get_median(list1, list2, length):
    merged_list = list1 + list2
    merged_list.sort()
    return (merged_list[int(length/2)-1] + merged_list[int(length/2)]) / 2


