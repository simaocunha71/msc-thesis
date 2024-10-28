def max_difference(list_tup):
    max_diff = 0
    for i in range(len(list_tup)):
        for j in range(i + 1, len(list_tup)):
            diff = max(list_tup[i][0], list_tup[i][1]) - min(list_tup[j][0], list_tup[j][1])
            if diff > max_diff:
                max_diff = diff
    return max_diff