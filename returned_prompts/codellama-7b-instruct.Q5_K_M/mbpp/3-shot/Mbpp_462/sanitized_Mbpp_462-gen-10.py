def combinations_list(input_list):
    if len(input_list) == 0:
        return []
    elif len(input_list) == 1:
        return [input_list]
    else:
        combos = []
        for i in range(len(input_list)):
            combos += [ [input_list[i]] + rest for rest in combinations_list(input_list[:i] + input_list[i+1:]) ]
        return combos