def max_difference(list_tuples):
    max_diff = 0
    for i in range(len(list_tuples)):
        for j in range(i+1, len(list_tuples)):
            diff = max(list_tuples[i][0], list_tuples[i][1]) - min(list_tuples[j][0], list_tuples[j][1])
            if diff > max_diff:
                max_diff = diff
    return max_diff