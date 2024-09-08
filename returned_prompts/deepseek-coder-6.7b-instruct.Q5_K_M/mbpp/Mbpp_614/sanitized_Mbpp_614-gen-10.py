def cummulative_sum(lst):
    total_sum = 0
    for tup in lst:
        total_sum += sum(tup)
    return total_sum