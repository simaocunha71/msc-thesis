def max_difference(tuples: list) -> int:
    max_diff = 0
    for i in range(len(tuples)):
        for j in range(i+1, len(tuples)):
            diff = abs(tuples[i][0] - tuples[j][0])
            max_diff = max(max_diff, diff)
    return max_diff