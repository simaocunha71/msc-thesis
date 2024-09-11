from itertools import combinations
def find_combinations(tuples):
    combinations_list = []
    for i in range(len(tuples)):
        for j in range(i+1, len(tuples)):
            combinations_list.append((tuples[i][0] + tuples[j][0], tuples[i][1] + tuples[j][1]))
    return combinations_list