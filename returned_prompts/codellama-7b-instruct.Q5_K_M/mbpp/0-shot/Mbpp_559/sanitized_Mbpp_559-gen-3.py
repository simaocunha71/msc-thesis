def max_sub_array_sum(my_list, n):
    max_sum = 0
    current_sum = 0
    for i in range(n):
        current_sum = max(current_sum + my_list[i], my_list[i])
        max_sum = max(max_sum, current_sum)
    return max_sum