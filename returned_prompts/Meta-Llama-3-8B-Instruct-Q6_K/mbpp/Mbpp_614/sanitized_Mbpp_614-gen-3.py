def cummulative_sum(tup_list):
    total = 0
    for tup in tup_list:
        for num in tup:
            total += num
    return total