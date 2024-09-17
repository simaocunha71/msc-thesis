def max_difference(tuple_list: list) -> int:
    max_diff = 0
    for i in range(len(tuple_list)):
        for j in range(i + 1, len(tuple_list)):
            if abs(tuple_list[i][1] - tuple_list[j][0]) > max_diff:
                max_diff = abs(tuple_list[i][1] - tuple_list[j][0])
    return max_diff