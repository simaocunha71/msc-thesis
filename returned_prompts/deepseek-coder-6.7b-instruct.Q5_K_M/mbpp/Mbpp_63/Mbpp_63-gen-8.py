def max_difference(tuples):
    max_diff = 0
    for i in range(len(tuples)):
        for j in range(i+1, len(tuples)):
            diff = abs(tuples[i][0] - tuples[j][0]) + abs(tuples[i][1] - tuples[j][1])
            if diff > max_diff:
                max_diff = diff
    return max_diff

print(max_difference([(3, 5), (1, 7), (10, 3), (1, 2)]))  # 7



