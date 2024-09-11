from itertools import izip, chain
def pair_wise(lst):
    return list(chain(*[izip(lst, lst[1:])]*len(lst)))