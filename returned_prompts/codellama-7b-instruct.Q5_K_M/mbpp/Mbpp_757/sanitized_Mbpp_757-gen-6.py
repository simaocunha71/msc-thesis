from itertools import combinations
from itertools import product
def count_reverse_pairs(strings):
    pairs = combinations(product(strings, strings), 2)
    return sum(p[0] == p[1][::-1] for p in pairs)