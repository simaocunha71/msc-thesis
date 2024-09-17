def combinations_list(input_list):
    if len(input_list) == 0:
        return [[]]
    result = []
    for i, element in enumerate(input_list):
        rest = input_list[i + 1:]
        for combination in combinations_list(rest):
            result.append([element] + combination)
    return result