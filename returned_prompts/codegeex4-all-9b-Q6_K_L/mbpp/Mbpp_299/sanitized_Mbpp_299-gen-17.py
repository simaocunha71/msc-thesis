def max_aggregate(tup_list: list) -> tuple:
    max_tup = tup_list[0]
    max_sum = sum(tup[1] for tup in tup_list if tup[0] == max_tup[0])
    for tup in tup_list:
        current_sum = sum(tup[1] for tup in tup_list if tup[0] == tup[0])
        if current_sum > max_sum:
            max_sum = current_sum
            max_tup = tup
    return max_tup