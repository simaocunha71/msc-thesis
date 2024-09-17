from itertools import combinations
def find_combinations(lst):
    result = []
    for i in range(1, len(lst)+1):
        result.extend([(sum(x[0] for x in comb), sum(x[1] for x in comb)) for comb in combinations(lst, i)])
    return result