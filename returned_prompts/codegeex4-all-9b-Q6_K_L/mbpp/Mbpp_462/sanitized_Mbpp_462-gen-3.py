def combinations_list(lst):
    result = [[]]
    for item in lst:
        result.extend([comb + [item] for comb in result])
    return result