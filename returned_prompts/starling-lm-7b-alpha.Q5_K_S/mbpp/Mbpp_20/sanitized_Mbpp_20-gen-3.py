from collections import Counter
from math import sqrt, log
def is_woodall(n):
    str_n = str(n)
    rev_str_n = str_n[::-1]
    return str_n == rev_str_n