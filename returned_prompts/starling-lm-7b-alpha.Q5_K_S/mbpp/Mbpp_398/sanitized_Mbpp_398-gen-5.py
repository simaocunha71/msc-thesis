from functools import reduce
from itertools import chain, imap
def sum_of_digits(numbers):
    s = 0
    for i in numbers:
        while i > 0:
            s += i % 10
            i = i // 10
    return s