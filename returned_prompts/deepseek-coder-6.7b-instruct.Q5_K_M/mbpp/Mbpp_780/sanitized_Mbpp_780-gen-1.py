from itertools import combinations
def find_combinations(tuples_list):
    result = []
    for i in range(2, len(tuples_list)+1):
        for comb in combinations(tuples_list, i):
            result.append(tuple(map(sum, zip(*comb))))
    return result