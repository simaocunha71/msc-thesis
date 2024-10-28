from hypothesis import given, settings, assume
from hypothesis.strategies import lists, integers
def nth_nums(lst,n):
    return [pow(i,n) for i in lst]