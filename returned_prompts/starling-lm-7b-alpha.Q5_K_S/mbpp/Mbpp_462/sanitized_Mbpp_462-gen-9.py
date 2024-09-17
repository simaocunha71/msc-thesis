def combinations_list(lst):
    """Find all possible combinations of the elements of a given list"""
    if len(lst) == 0:
        return [[]]
    if len(lst) == 1:
        return [lst, []]
    sub_combinations = combinations_list(lst[1:])
    combinations = []
    for combination in sub_combinations:
        combinations.append(combination)
        combinations.append([lst[0]] + combination)
    return combinations