"""
def find_combinations(tuples):
    combinations = []
    for i in range(len(tuples)):
        for j in range(i + 1, len(tuples)):
            combinations.append((tuples[i][0] + tuples[j][0], tuples[i][1] + tuples[j][1]))
            combinations.append((tuples[i][0] + tuples[j][1], tuples[i][1] + tuples[j][0]))
            combinations.append((tuples[i][1] + tuples[j][0], tuples[i][0] + tuples[j][1]))
            combinations.append((tuples[i][1] + tuples[j][1], tuples[i][0] + tuples[j][0]))
    return combinations

assert find_combinations([(2, 4), (6, 7), (5, 1), (6, 10)]) == [(8, 11), (7, 5), (8, 14), (11, 8), (12, 17), (11, 11)]
"""

