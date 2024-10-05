
from hashlib import md5

def string_to_md5(text):
    if not text:
        return None
    else:
        hasher = md5()
        hasher.update(text.encode('utf-8'))
        return hasher.hexdigest()


























```
from __future__ import division
from collections import defaultdict, Counter
from math import log, factorial




def gcd(x, y):
    """greatest common divisor of x and y"""
    while y:
        x, y = y, x % y
    return x

def memodict(f):
    """memoization decorator for a function taking a single argument"""
    class memodict(dict):
        def __missing__(self, key):
            ret = self[key] = f(key)
            return ret
    return memodict().__getitem__








































def is_prime(n):
    """returns True if n is prime else False"""
    if n < 4:
        return bool(n)
    if n % 2 == 0:
        return False
    if n % 3 == 0:
        return False
    i = 5
    w = 2
    while i * i <= n:
        if n % i == 0:
            return False
        i += w
        w = 6 - w
    return True


```