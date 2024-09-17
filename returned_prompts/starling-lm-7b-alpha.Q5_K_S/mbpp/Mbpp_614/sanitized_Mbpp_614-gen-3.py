def cummulative_sum(tuple_list):
    total = 0
    for tup in tuple_list:
        total += sum(tup)
    return total