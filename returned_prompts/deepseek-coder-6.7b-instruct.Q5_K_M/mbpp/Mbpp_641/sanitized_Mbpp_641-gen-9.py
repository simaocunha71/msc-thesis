import unittest
from nonagonal import is_nonagonal
def is_nonagonal(n):
    return n*(7*n - 5)//2