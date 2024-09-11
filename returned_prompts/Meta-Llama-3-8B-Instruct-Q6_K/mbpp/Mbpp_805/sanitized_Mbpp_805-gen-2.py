def max_sum_list(list_of_lists):
    max_sum = max(sum(lst) for lst in list_of_lists)
    return [lst for lst in list_of_lists if sum(lst) == max_sum][0]  # This will return the first list that has the maximum sum, in case of multiple lists having the same sum. If you want to return all such lists, you can return [lst for lst in list_of_lists if sum(lst) == max_sum].