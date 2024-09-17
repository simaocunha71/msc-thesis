
def get_median(list1, list2, k):
    combined_list = sorted(list1 + list2)
    median = (combined_list[k-1] + combined_list[k]) / 2.0
    return median


