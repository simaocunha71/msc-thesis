def combinations_list(my_list):
    if len(my_list) == 0:
        return [[]]
    else:
        combos = []
        for i in range(len(my_list)):
            rest = my_list[:i] + my_list[i+1:]
            combos += [[my_list[i]] + c for c in combinations_list(rest)]
        return combos
