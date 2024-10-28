def find_combinations(tuple_list):
    combinations = set()
    for i in range(len(tuple_list)):
        for j in range(i, len(tuple_list)):
            combinations.add(tuple(sorted([tuple_list[i][0] + tuple_list[j][0], tuple_list[i][1] + tuple_list[j][1]])))
    return list(combinations)