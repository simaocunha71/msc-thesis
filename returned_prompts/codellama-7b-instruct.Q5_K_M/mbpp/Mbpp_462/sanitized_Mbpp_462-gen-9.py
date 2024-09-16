def combinations_list(my_list):
    if not my_list:
        return [[]]
    else:
        rest = combinations_list(my_list[1:])
        return [[my_list[0]] + r for r in rest] + rest