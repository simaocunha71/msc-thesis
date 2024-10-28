
def find_combinations(test_tup):
    combinations = []
    for i in range(len(test_tup)):
        for j in range(i+1, len(test_tup)):
            combinations.append((test_tup[i][0]+test_tup[j][0], test_tup[i][1]+test_tup[j][1]))
    return combinations


