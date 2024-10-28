from itertools import combinations
from itertools import combinations
def find_combinations(tuples_list):
    result = []
    for i in range(len(tuples_list)):
        for j in combinations(tuples_list[i], 2):
            result.append(tuple(j))
    return result