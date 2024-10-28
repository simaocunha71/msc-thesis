
def double_the_difference(lst):
    if len(lst) == 0:
        return 0
    else:
        lst = [i for i in lst if i >= 0 and i % 2 != 0]
        return sum([i**2 for i in lst])
    