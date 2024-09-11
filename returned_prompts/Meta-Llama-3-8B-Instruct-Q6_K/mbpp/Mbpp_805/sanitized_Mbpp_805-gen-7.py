def max_sum_list(list_of_lists):
    max_sum = max(sum(lst) for lst in list_of_lists)
    return [lst for lst in list_of_lists if sum(lst) == max_sum] [0]  # Return the first list that has the max sum