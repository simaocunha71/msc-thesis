def max_difference(tuple_list):
    # Find max difference
    max_diff = 0
    for i in range(len(tuple_list)):
        for j in range(i+1, len(tuple_list)):
            if tuple_list[j][0] - tuple_list[i][0] > max_diff:
                max_diff = tuple_list[j][0] - tuple_list[i][0]
    return max_diff