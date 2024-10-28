def combinations_list(input_list):
    result = [[]]
    for item in input_list:
        result += [curr + [item] for curr in result]
    return result