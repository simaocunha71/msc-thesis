from functools import reduce
from operator import xor
def pair_xor_Sum(L,n):
    return reduce(xor,L)*n
L=[5,9,7,6]
n=4