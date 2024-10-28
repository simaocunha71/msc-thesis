def cummulative_sum(tuple_list):
    cummulative_sum = 0
    for t in tuple_list:
        for value in t:
            cummulative_sum += value
    return cummulative_sum