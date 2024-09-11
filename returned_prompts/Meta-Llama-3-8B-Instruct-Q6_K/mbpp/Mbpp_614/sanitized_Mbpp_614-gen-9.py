def cummulative_sum(tup_list):
    cumulative_sum = 0
    for tup in tup_list:
        for num in tup:
            cumulative_sum += num
    return cumulative_sum