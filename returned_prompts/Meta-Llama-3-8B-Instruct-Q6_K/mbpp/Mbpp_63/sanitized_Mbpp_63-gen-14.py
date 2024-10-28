def max_difference(tuple_list):
    max_diff = 0
    for i in range(len(tuple_list)):
        for j in range(i+1, len(tuple_list)):
            diff = abs(tuple_list[i][0] - tuple_list[j][1])
            max_diff = max(max_diff, diff)
    return max_diff