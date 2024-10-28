def cummulative_sum(tuple_list):
    total = 0
    for tuple_ in tuple_list:
        total += sum(tuple_)
    return total