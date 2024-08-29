def cummulative_sum(tuple_list):
    sum = 0
    for tup in tuple_list:
        for num in tup:
            sum += num
    return sum