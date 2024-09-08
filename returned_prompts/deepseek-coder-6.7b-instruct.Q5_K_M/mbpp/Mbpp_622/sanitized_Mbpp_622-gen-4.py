def get_median(list1, list2, size):
    new_list = sorted(list1 + list2)
    if size % 2 != 0:
        return new_list[size//2]
    else:
        return (new_list[size//2] + new_list[(size//2) - 1]) / 2