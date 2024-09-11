def max_sum_list(list_of_lists):
    max_sum = 0
    max_sum_list = []
    for sublist in list_of_lists:
        curr_sum = sum(sublist)
        if curr_sum > max_sum:
            max_sum = curr_sum
            max_sum_list = sublist
    return max_sum_list
list_of_lists = [[1, 2, 3], [4, 5, 6], [10, 11, 12], [7, 8, 9]]