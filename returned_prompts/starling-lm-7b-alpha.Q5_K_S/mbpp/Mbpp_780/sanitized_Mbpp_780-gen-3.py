def find_combinations(tuples):
    result = []
    for i in range(len(tuples)):
        for j in range(i+1, len(tuples)):
            result.append((tuples[i][0]+tuples[j][0], tuples[i][1]+tuples[j][1]))
    return result