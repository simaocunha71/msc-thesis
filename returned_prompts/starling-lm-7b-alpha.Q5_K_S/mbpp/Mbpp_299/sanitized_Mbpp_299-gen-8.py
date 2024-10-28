def max_aggregate(tup_list):
    max_tup = tup_list[0]
    for i in tup_list:
        if i[1] > max_tup[1]:
            max_tup = i
    return max_tup