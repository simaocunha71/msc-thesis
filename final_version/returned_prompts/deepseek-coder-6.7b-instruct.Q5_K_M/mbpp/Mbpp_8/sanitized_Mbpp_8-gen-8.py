import math
def square_nums(lst):
    return list(map(math.pow, lst, [2]*len(lst)))