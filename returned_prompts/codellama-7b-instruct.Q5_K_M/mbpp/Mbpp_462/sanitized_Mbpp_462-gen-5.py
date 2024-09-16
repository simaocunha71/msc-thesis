def combinations_list(my_list):
    if my_list == []:
        return [[]]
    else:
        return [[item] + sub_combinations for sub_combinations in combinations_list(my_list[1:]) for item in [my_list[0]]]