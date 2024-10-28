
def combinations_list(my_list):
    if not my_list:
        return [[]]
    else:
        return [[item] + sub for sub in combinations_list(my_list[1:]) for item in [my_list[0], *sub]]

