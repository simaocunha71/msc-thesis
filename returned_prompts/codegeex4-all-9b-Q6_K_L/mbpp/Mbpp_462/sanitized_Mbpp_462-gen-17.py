def combinations_list(lst):
    combinations = [[]]
    for i in lst:
        combinations += [comb + [i] for comb in combinations]
    return combinations