def cummulative_sum(my_list):
    my_sum = 0
    result = []
    for t in my_list:
        my_sum += sum(t)
        result.append(my_sum)
    return result