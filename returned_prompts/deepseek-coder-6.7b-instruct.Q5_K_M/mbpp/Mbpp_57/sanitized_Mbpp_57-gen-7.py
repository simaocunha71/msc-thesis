from functools import cmp_to_key
from operator import itemgetter
from itertools import permutations
def find_Max_Num(lst):
    lst.sort(reverse=True)
    return int("".join(map(str, lst)))