def find_combinations(lst):
    all_combinations = []
    for i in range(len(lst)):
        for j in range(i+1, len(lst)):
            all_combinations.append((lst[i][0]+lst[j][0], lst[i][1]+lst[j][1]))
    return all_combinations