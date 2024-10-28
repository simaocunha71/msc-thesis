
def double_the_difference(lst):
    lst = list(filter(lambda x: x >= 0 and x % 1 == 0, lst))
    lst = list(map(lambda x: x * 2, lst))
    return sum(lst)
