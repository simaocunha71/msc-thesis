import itertools
def find_combinations(lst):
    combs = list(itertools.product(*lst))
    return [(sum(x), sum(y)) for x, y in combs]