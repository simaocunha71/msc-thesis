def cummulative_sum(tuple_list):
    total_sum = 0
    for i in tuple_list:
        total_sum += sum(i)
    return total_sum