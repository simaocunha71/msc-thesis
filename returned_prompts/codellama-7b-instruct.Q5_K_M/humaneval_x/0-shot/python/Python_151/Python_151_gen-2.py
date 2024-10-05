
def double_the_difference(lst):
    if not lst:
        return 0
    lst = [x for x in lst if x > 0 and x % 1 == 0]
    lst = [x*2 for x in lst]
    return sum(lst)