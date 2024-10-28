def combinations_list(lst: list) -> list:
    return [comb for i in range(len(lst)+1) for comb in itertools.combinations(lst, i)]