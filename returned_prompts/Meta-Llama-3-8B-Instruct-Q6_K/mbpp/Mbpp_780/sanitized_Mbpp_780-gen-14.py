def find_combinations(tuples_list):
    result = []
    for i in range(len(tuples_list)):
        for j in range(i, len(tuples_list)):
            result.append((tuples_list[i][0] + tuples_list[j][0], tuples_list[i][1] + tuples_list[j][1]))
    return result