def find_combinations(tup_list):
    result = []
    for tup1 in tup_list:
        for tup2 in tup_list:
            result.append((tup1[0]+tup2[0], tup1[1]+tup2[1]))
    return result
tup_list = [(2, 4), (6, 7), (5, 1), (6, 10)]