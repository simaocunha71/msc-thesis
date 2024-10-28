def max_difference(tup_list):
    return max(abs(tup[0] - tup[1]) for tup in tup_list)