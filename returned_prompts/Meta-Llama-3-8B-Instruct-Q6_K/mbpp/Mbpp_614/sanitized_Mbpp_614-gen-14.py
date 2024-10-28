def cummulative_sum(tup_list):
    cum_sum = 0
    for tup in tup_list:
        for val in tup:
            cum_sum += val
    return cum_sum