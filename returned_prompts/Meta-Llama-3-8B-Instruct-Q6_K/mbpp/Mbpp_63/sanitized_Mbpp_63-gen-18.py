def max_difference(tuple_list):
    max_diff = 0
    for i in range(len(tuple_list)):
        for j in range(i+1, len(tuple_list)):
            diff = abs(tuple_list[i][1] - tuple_list[j][0])
            if diff > max_diff:
                max_diff = diff
    return max_diff