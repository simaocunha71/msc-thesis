def combinations_list(my_list):
    if not my_list:
        return [[]]
    else:
        combos = []
        for i in range(len(my_list)):
            for c in combinations_list(my_list[i+1:]):
                combos.append([my_list[i]] + c)
        return combos