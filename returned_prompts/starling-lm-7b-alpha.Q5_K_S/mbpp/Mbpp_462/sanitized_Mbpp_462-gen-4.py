from itertools import chain, product
def combinations_list(lst):
    combos = [[]]
    for elem in lst:
        combos += [comb + [elem] for comb in combos]
    return combos