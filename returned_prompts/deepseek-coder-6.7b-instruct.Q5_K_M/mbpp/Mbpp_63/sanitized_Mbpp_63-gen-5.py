def max_difference(tuples):
    maximum = 0
    for i in range(len(tuples)):
        for j in range(i+1, len(tuples)):
            difference = abs(tuples[i][0] - tuples[j][0])
            if difference > maximum:
                maximum = difference
    return maximum