def combinations_list(input_list):
    if len(input_list) == 0:
        return [[]]
    combinations = combinations_list(input_list[1:])
    return combinations + [x + [input_list[0]] for x in combinations]