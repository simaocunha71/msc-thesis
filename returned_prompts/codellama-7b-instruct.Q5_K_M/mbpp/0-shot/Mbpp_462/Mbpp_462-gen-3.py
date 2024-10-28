
def combinations_list(my_list):
    if not my_list:
        return [[]]
    else:
        current = my_list[0]
        rest = my_list[1:]
        with_current = [[current] + rest for rest in combinations_list(rest)]
        without_current = combinations_list(rest)
        return with_current + without_current
