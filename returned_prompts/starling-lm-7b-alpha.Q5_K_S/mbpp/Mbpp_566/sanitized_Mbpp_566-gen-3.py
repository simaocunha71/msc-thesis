from functools import reduce
from operator import itemgetter
def sum_digits(n):
    return sum(map(int, str(n)))