def get_median(list1, list2, size):
    # Merge the two lists
    merged_list = sorted(list1 + list2)
    
    # Find the median
    if size % 2 == 1:
        return merged_list[size // 2]
    else:
        return (merged_list[size // 2 - 1] + merged_list[size // 2]) / 2