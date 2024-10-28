def max_difference(tuples):
    max_diff = 0
    for i in range(len(tuples)):
        for j in range(i + 1, len(tuples)):
            if tuples[i][1] < tuples[j][0]:
                diff = tuples[j][0] - tuples[i][1]
                if diff > max_diff:
                    max_diff = diff
    return max_diff