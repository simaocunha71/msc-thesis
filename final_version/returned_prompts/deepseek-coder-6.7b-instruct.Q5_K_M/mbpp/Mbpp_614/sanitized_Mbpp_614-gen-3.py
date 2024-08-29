def cummulative_sum(tuples):
    total = 0
    for t in tuples:
        for num in t:
            total += num
    return total