def find_combinations(my_tuple_list):
    combinations = []
    for i in range(len(my_tuple_list)):
        for j in range(i+1, len(my_tuple_list)):
            combinations.append((my_tuple_list[i][0] + my_tuple_list[j][0], my_tuple_list[i][1] + my_tuple_list[j][1]))
    return combinations