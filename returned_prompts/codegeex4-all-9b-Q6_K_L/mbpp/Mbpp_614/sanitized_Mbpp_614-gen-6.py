def cummulative_sum(lst):
    total = 0
    for tup in lst:
        total += sum(tup)
    return total