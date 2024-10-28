
def double_the_difference(lst):
    lst = list(map(lambda x: x**2, lst))
    lst = list(filter(lambda x: x > 0, lst))
    return sum(lst)
