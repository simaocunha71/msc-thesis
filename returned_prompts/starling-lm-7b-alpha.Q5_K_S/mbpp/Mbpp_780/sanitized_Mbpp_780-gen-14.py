def find_combinations(tuples):
    result = []
    for i in range(len(tuples)):
        for j in range(i + 1, len(tuples)):
            result.append(sum(tuples[i], tuples[j]))
    return result