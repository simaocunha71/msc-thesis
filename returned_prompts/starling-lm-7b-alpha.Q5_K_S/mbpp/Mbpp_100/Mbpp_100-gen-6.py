"""
from math import log10 as log

def next_smallest_palindrome(n):
    if n < 10:
        return n+1
    if n < 100:
        if n%11 == 0:
            return n+9-n%11
        else:
            return n+11-n%11
    if n < 1000:
        if n%11 == 0:
            return n+99-n%11
        elif int(log(n, 11)) % 2 == 0:
            return n+111-n%11
        else:
            return n+101-n%11
    if n < 10000:
        if n%11 == 0:
            return n+999-n%11
        elif int(log(n, 11)) % 2 == 0:
            return n+1111-n%11
        else:
            return n+1011-n%11
    if n < 100000:
        if n%11 == 0:
            return n+9999-n%11
        elif int(log(n, 11)) % 2 == 0:
            return n+11111-n%11
        else:
            return n+10111-n%11
    if n < 1000000:
        if n%11 == 0:
            return n+99999-n%11
        elif int(log(n, 11)) % 2 == 0:
            return n+111111-n%11
        else:
            return n+101111-n%11
    if n < 10000000:
        if n%11 == 0:
            return n+999999-n%11
        elif int(log(n, 11)) % 2 == 0:
            return