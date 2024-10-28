def cummulative_sum(tuples_list):
    result = 0
    for t in tuples_list:
        result += sum(t)
    return result