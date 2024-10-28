def get_median(list1, list2, size):
    combined_list = list1 + list2
    combined_list.sort()
    if len(combined_list) % 2 == 1:  # Odd length
        return combined_list[len(combined_list) // 2]
    else:  # Even length
        return (combined_list[len(combined_list) // 2 - 1] + combined_list[len(combined_list) // 2]) / 2