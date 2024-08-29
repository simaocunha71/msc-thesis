def get_median(list1, list2, n):
    new_list = sorted(list1 + list2)
    return (new_list[n-1] + new_list[n]) / 2.0